"""Quick runner for case 5 on models that missed it."""
import os, datetime
from pathlib import Path
from openai import OpenAI

API_KEY = "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"

notes = "api — timeout\nfix by 5pm\nnadh said no\nwssdk — ??"

SYSTEM = """You are a knowledge management assistant. Convert raw, unstructured notes into structured, clean Markdown knowledge-base entries suitable for an Obsidian wiki.

Critical rules:
1. If the notes contain conflicting information, flag the conflict explicitly instead of silently picking one side.
2. If the notes mix unrelated topics (business + personal), split them into separate entries or flag what's out of scope.
3. If the notes are too sparse or cryptic to produce a meaningful entry, say so clearly and list what information is missing.
4. Always preserve names, dates, and deadlines exactly as stated.
5. Use Obsidian-style [[wikilinks]] for key entities, projects, and concepts.
6. NEVER invent or hallucinate details not present in the notes. "nadh" is a person's name, not the NADH molecule. "wssdk" likely refers to a software SDK, not a chemical. If you don't know what something means, say so. Only use information explicitly stated in the notes."""

USER = """Convert the following raw notes into a structured knowledge-base entry. Your output MUST follow this format exactly:

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
  NOTE: Only create action items that are explicitly stated or clearly implied. Do NOT invent tasks.

## Notes on Data Quality
Brief note on any conflicts, ambiguities, or items needing human review.

## Related
- [[Related topic or project]]

Here are the notes:

{notes}"""

models = ["minimax/minimax-m2.5:free", "qwen/qwen3.6-plus:free"]
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=API_KEY)

for model in models:
    print(f"\n{'='*40}\n=== {model} ===\n{'='*40}\n")
    try:
        r = client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": SYSTEM},
                      {"role": "user", "content": USER.format(notes=notes)}],
            temperature=0.3, max_tokens=1500
        )
        out = r.choices[0].message.content
        short = model.split("/")[-1].replace(":", "_")
        out_path = f"outputs/case_5_edge_sparse_v3_{short}_output.md"
        # Save with eval_set header
        Path(out_path).write_text(
            f"# case_5_edge_sparse\n**Category:** edge\n**Description:** Very sparse/cryptic notes\n**Prompt version:** v3\n\n"
            f"## Raw Input\n```\n{notes}\n```\n\n"
            f"## Expected Behavior\nShould recognize insufficient context and NOT hallucinate.\n\n"
            f"## LLM Output\n{out}\n"
        )
        print(f"Saved to {out_path}")
        print(f"\nOutput (first 200 chars):\n{out[:200]}...\n")
    except Exception as e:
        print(f"Error: {e}")
