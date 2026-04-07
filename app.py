"""
app.py — Notes to Knowledge-Base Entry Generator

Converts raw, unstructured notes into structured, Obsidian-compatible
knowledge-base entries using an LLM via OpenRouter.

Usage:
    python app.py                  # runs evaluation on all cases
    python app.py run              # interactive mode, paste notes
    python app.py eval             # run full evaluation suite
    python app.py prompt v1|v2|v3  # test specific prompt version
"""

import os
import json
import datetime
from pathlib import Path
from openai import OpenAI


MODELS = [
    "nvidia/nemotron-3-super-120b-a12b:free",
    "qwen/qwen2.5-72b-instruct:free",
    "google/gemma-3-12b-it:free",
    "meta-llama/llama-3.1-8b-instruct:free",
]

PROMPTS = {
    "v1": {
        "system": "You are a helpful assistant that converts raw notes into structured knowledge-base entries.",
        "user": "Convert these notes into a structured knowledge-base entry:\n\n{notes}\n\nFormat the output with a title, summary, and any key points.",
    },
    "v2": {
        "system": "You are a knowledge management assistant. Your job is to convert raw, unstructured notes (meeting notes, Slack messages, brain-storms) into structured, clean Markdown knowledge-base entries suitable for an Obsidian wiki.",
        "user": """Convert the following raw notes into a structured knowledge-base entry. Your output must follow this format exactly:

# Entry Title
## Summary
A 2-3 sentence summary of the key information.
## Key Details
- Bullet points of important details
## Action Items
- [ ] Action item (who: name, deadline: date)
## Tags
#tag1 #tag2 #tag3

Here are the notes:

{notes}""",
    },
    "v3": {
        "system": "You are a knowledge management assistant. Convert raw, unstructured notes into structured, clean Markdown knowledge-base entries suitable for an Obsidian wiki.\n\nCritical rules:\n1. If the notes contain conflicting information, flag the conflict explicitly instead of silently picking one side.\n2. If the notes mix unrelated topics (business + personal), split them into separate entries or flag what's out of scope.\n3. If the notes are too sparse or cryptic to produce a meaningful entry, say so clearly and list what information is missing.\n4. Always preserve names, dates, and deadlines exactly as stated.\n5. Use Obsidian-style [[wikilinks]] for key entities, projects, and concepts.\n6. NEVER invent or hallucinate details not present in the notes. \"nadh\" is a person's name, not the NADH molecule. \"wssdk\" likely refers to a software SDK, not a chemical. If you don't know what something means, say so. Only use information explicitly stated in the notes.",
        "user": """Convert the following raw notes into a structured knowledge-base entry. Your output MUST follow this format exactly:

---
title: Auto-generated title
date: YYYY-MM-DD
type: meeting-notes | decision | tech-note | brainstorm
tags: [tag1, tag2, tag3]
---

# [[Title]]

## Summary
A concise 2-3 sentence summary.

## Key Details
- Bullet points of important facts and decisions
- Preserve names, dates, and specific values exactly

## Action Items
- [ ] Task description (assigned to: name, deadline: date if known)
  NOTE: Only create action items that are explicitly stated or clearly implied in the notes. Do NOT invent tasks.

## Notes on Data Quality
<!-- If there are contradictions, missing info, or mixed topics, note them here. Otherwise leave brief. -->
Brief note on any conflicts, ambiguities, or items needing human review.

## Related
- [[Related topic or project]]

Here are the notes:

{notes}""",
    },
}


EVAL_CASES = {
    "case_1_normal": {
        "category": "normal",
        "description": "Rough meeting notes about onboarding flow bugs",
        "notes": (
            "synced with arjun re: onboarding flow today. "
            "main issues: users dropping off at phone verification step "
            "(OTP delays). solution: maybe add fallback to email verification? "
            "also need to update welcome message template — current one is too long. "
            "arjun said he'll handle the OTP part by fri. "
            "i'll update the welcome msg by wed. "
            "also flagged the analytics dashboard is showing stale data — "
            "backend team needs to look at it."
        ),
        "expected": (
            "Should extract action items with owners and deadlines, "
            "tag as meeting-notes, and produce a clean summary."
        ),
    },
    "case_2_normal": {
        "category": "normal",
        "description": "Slack thread about WhatsApp API rate limits",
        "notes": (
            "slack convo from #dev channel. "
            "nadh: hey the whatsapp api rate limit is hitting us on pro tier. "
            "me: right now we're using the standard cloud api with no queue. "
            "nadh: can we add a message queue? "
            "me: yeah redis queue should work, we can throttle to 80msg/sec per WABA. "
            "nadh: ok spike it and let me know by tmr. "
            "also — the PII masking middleware is leaking phone numbers in logs. "
            "severity: high."
        ),
        "expected": (
            "Should capture the technical issue, proposed solution (Redis queue), "
            "flag the high-severity PII leak, and create action items."
        ),
    },
    "case_3_edge_mixed": {
        "category": "edge",
        "description": "Mixed-topic brain dump (business + personal)",
        "notes": (
            "random things on my mind today: "
            "the omagent pricing tiers might need adjusting — enterprise at 25k feels low. "
            "also need to fix the docker compose file it keeps failing on m1. "
            "oh and reminder: call dentist at 3pm wednesday. "
            "the new gemma model from google is surprisingly good for tool use, "
            "should test it in sri-workflow. "
            "my phone battery dying too fast."
        ),
        "expected": (
            "Should NOT merge everything into one entry. "
            "Good output: splits into separate entries (business/tech vs personal), "
            "or flags personal items as out of scope."
        ),
    },
    "case_4_hard_contradiction": {
        "category": "hard_fail",
        "description": "Conflicting client meeting notes",
        "notes": (
            "client meeting notes — freshtech: "
            "they want a hotel bot for sure. contract starts next monday march 10. "
            "budget is 15k, 3-month deal. contact person is priya.\n"
            "---\n"
            "follow-up email to priya at freshtech: "
            "she said they want a clinic bot instead. timeline is end of april. "
            "budget now 25k. waiting on their CTO to confirm."
        ),
        "expected": (
            "Should FLAG the contradiction (hotel vs clinic, 15k vs 25k, "
            "march vs april) and NOT silently pick one side. "
            "Should recommend human review."
        ),
    },
    "case_5_edge_sparse": {
        "category": "edge",
        "description": "Very sparse/cryptic notes",
        "notes": (
            "api — timeout\n"
            "fix by 5pm\n"
            "nadh said no\n"
            "wssdk — ??"
        ),
        "expected": (
            "Should recognize insufficient context, list what can be partially "
            "extracted, and ask for clarification rather than hallucinating details."
        ),
    },
}


def call_llm(notes: str, prompt_version: str = "v3", model: str = "nvidia/nemotron-3-super-120b-a12b:free") -> str:
    """Send notes to the LLM and return the generated knowledge-base entry."""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY environment variable not set. "
            "Run: export OPENROUTER_API_KEY='your-key-here'"
        )

    prompt = PROMPTS[prompt_version]
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": prompt["system"]},
            {"role": "user", "content": prompt["user"].format(notes=notes)},
        ],
        temperature=0.3,
        max_tokens=1500,
    )

    return response.choices[0].message.content


def run_evaluation(prompt_version: str = "v3", model: str = None):
    """Run the LLM on all evaluation cases and save outputs."""
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    model = model or "nvidia/nemotron-3-super-120b-a12b:free"

    results = {}

    model_short = model.split("/")[-1].replace(":", "_")
    print(f"{'='*60}")
    print(f"Running evaluation with prompt {prompt_version}")
    print(f"Model: {model}")
    print(f"Timestamp: {timestamp}")
    print(f"{'='*60}\n")

    for case_id, case_data in EVAL_CASES.items():
        print(f"--- Processing {case_id} ({case_data['category']}) ---")
        print(f"Input preview: {case_data['notes'][:80]}...\n")

        try:
            result = call_llm(case_data["notes"], prompt_version, model)
            results[case_id] = {
                "status": "success",
                "output": result,
                "expected": case_data["expected"],
                "category": case_data["category"],
                "notes": case_data["notes"],
            }

            # Save individual output
            out_file = output_dir / f"{case_id}_{prompt_version}_{model_short}_output.md"
            out_file.write_text(
                f"# {case_id}\n"
                f"**Category:** {case_data['category']}\n"
                f"**Description:** {case_data['description']}\n"
                f"**Prompt version:** {prompt_version}\n\n"
                f"## Raw Input\n```\n{case_data['notes']}\n```\n\n"
                f"## Expected Behavior\n{case_data['expected']}\n\n"
                f"## LLM Output\n{result}\n"
            )

            print(f"Saved to {out_file}")
            print(f"Output preview: {result[:120]}...\n")

        except Exception as e:
            print(f"Error processing {case_id}: {e}\n")
            results[case_id] = {
                "status": "error",
                "error": str(e),
                "expected": case_data["expected"],
                "category": case_data["category"],
            }

    # Save summary
    summary_file = output_dir / f"eval_summary_{prompt_version}_{model_short}_{timestamp}.json"
    summary = {
        "prompt_version": prompt_version,
        "model": model,
        "timestamp": timestamp,
        "total_cases": len(EVAL_CASES),
        "results": {
            k: {
                "status": v["status"],
                "category": v.get("category", ""),
                "error": v.get("error", ""),
            }
            for k, v in results.items()
        },
    }
    summary_file.write_text(json.dumps(summary, indent=2))
    print(f"Evaluation summary saved to {summary_file}")
    return results


def interactive_mode(prompt_version: str = "v3"):
    """Interactive mode: paste notes, get a knowledge-base entry."""
    print(f"Notes → Knowledge-Base Entry Generator (prompt {prompt_version})")
    print("Paste your notes below. Press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) when done.\n")

    try:
        notes = input()
    except (KeyboardInterrupt, EOFError):
        print("Aborted.")
        return

    try:
        result = call_llm(notes, prompt_version)
        print(f"\n{'='*60}")
        print("GENERATED KNOWLEDGE-BASE ENTRY")
        print(f"{'='*60}\n")
        print(result)
        print(f"\n{'='*60}")
    except Exception as e:
        print(f"Error: {e}")


def run_multi_model_comparison(prompt_version: str = "v3"):
    """Run evaluation across all free models and compare results."""
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    print(f"\n{'='*60}")
    print(f"Multi-model comparison with prompt {prompt_version}")
    print(f"Models to test: {len(MODELS)}")
    print(f"{'='*60}")

    all_results = {}
    for model in MODELS:
        print(f"\n{'~'*40}")
        print(f"Testing: {model}")
        print(f"{'~'*40}")
        model_short = model.split("/")[-1].replace(":", "_")
        results = run_evaluation(prompt_version, model)
        all_results[model_short] = {
            "model_id": model,
            "total": len(results),
            "success": sum(1 for r in results.values() if r["status"] == "success"),
            "errors": sum(1 for r in results.values() if r["status"] == "error"),
        }

    # Save comparison summary
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    comp_file = output_dir / f"model_comparison_{prompt_version}_{timestamp}.json"
    comp_file.write_text(json.dumps(all_results, indent=2))
    print(f"\n{'='*60}")
    print(f"Comparison summary:")
    for model_short, stats in all_results.items():
        print(f"  {model_short}: {stats['success']}/{stats['total']} successful")
    print(f"Full comparison saved to {comp_file}")
    return all_results



def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python app.py eval                          Run evaluation with v3 prompt (default model)")
        print("  python app.py run                           Interactive mode - paste notes")
        print("  python app.py prompt v1|v2|v3              Run evaluation with specific prompt")
        print("  python app.py model MODEL_ID               Run eval with specific model")
        print("  python app.py compare                       Run all free models, compare results")
        print("  python app.py list-models                   List available free models")
        print("")
        print("Available models:")
        for m in MODELS:
            print(f"  - {m}")
        return

    command = sys.argv[1]
    prompt_version = "v3"

    if command == "run":
        interactive_mode(prompt_version)
    elif command == "eval":
        run_evaluation(prompt_version)
    elif command == "prompt" and len(sys.argv) >= 3:
        prompt_version = sys.argv[2]
        if prompt_version not in PROMPTS:
            print(f"Unknown prompt version: {prompt_version}. Use v1, v2, or v3.")
            return
        run_evaluation(prompt_version)
    elif command == "compare":
        run_multi_model_comparison(prompt_version)
    elif command == "model" and len(sys.argv) >= 3:
        model = sys.argv[2]
        if model not in MODELS:
            print(f"Warning: {model} not in default model list. Trying anyway...")
        run_evaluation(prompt_version, model)
    elif command == "list-models":
        print("Available free models for evaluation:")
        for m in MODELS:
            print(f"  - {m}")
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
