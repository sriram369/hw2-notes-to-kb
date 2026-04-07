# Report: Notes to Knowledge-Base GenAI Workflow

## Business Use Case

This prototype converts raw, unstructured notes (meeting notes, Slack conversations, brain-storms) into structured, Obsidian-compatible knowledge-base entries. The target user is a technical team lead or founder who captures raw notes throughout the day but lacks a systematic way to organize them into searchable, well-structured reference material.

The workflow is valuable because:
1. **Time savings:** Manual note formatting and structuring is tedious and often skipped
2. **Knowledge retention:** Structured entries with tags and wikilinks make past decisions findable
3. **Consistency:** A uniform format means any team member can read any entry efficiently

## Model Selection

**Chosen model:** `qwen/qwen-2.5-72b-instruct` via OpenRouter (free tier).

**Why this model:** The Qwen 2.5 72B Instruct model offers strong instruction-following capabilities at zero cost through OpenRouter's free tier. It handles structured output well, which is critical for this task where we need consistent formatting with frontmatter, sections, and tags.

**Other models considered:** I briefly tested `meta-llama/llama-3.1-8b-instruct` (also free via OpenRouter) but found it struggled with the more complex formatting requirements, particularly YAML frontmatter and Obsidian wikilinks. The 72B model produced notably more consistent structured output.

## Prompt Iteration: Baseline vs. Final

### v1 (Baseline) — Free-form
Initial prompt was minimal: "convert these notes into a structured entry with title, summary, and key points." The output was inconsistent—sometimes it used markdown, sometimes plain text, and action items were rarely extracted.

### v2 — Added structure
I added explicit format requirements (title, summary, details, action items, tags). This immediately improved consistency: outputs now followed the same structure. However, two issues emerged: (1) the model silently resolved contradictions instead of flagging them, and (2) it tried to merge unrelated topics into forced coherence.

### v3 (Final) — Added conflict detection, frontmatter, and data quality awareness
Key additions: explicit rules for handling contradictions, mixed topics, and sparse notes; YAML frontmatter for Obsidian; a "Data Quality" section where the model flags its own uncertainty. This version correctly identified contradictions in Case 4 and refused to hallucinate details in Case 5.

### Summary of improvements:
| Metric | v1 | v2 | v3 |
|--------|-----|-----|-----|
| Format consistency | poor | good | excellent |
| Handles contradictions | fails silently | fails silently | flags explicitly |
| Handles mixed topics | merges poorly | merges poorly | splits/flags |
| Handles sparse notes | hallucinates | hallucinates | flags missing info |
| Obsidian-ready | no | partial | yes |

## Where the Prototype Still Fails

**Contradiction resolution remains a judgment call:** While the prototype now *flags* contradictions rather than silently picking sides, it doesn't *resolve* them. A human must still review conflicting notes and decide which version is correct. For example, in Case 4 (client meeting with conflicting budget/timeline), the model correctly identifies the discrepancy but cannot determine the actual deal terms.

**Sparse context can't be compensated:** When notes are too cryptic (Case 5), no amount of prompt engineering can recover missing information. The model correctly recognizes this and asks for clarification, but from a user experience standpoint, a real product would need a better interaction model than "sorry, I need more context."

**Date parsing is fragile:** The model tries to infer dates from relative references ("next Monday," "by Friday"), but without knowing the current date, it sometimes guesses wrong. Passing a reference date would help.

## Deployment Recommendation

I would **recommend deploying this workflow with human-in-the-loop review**. The prototype works well for Case 1 and 2 (standard meeting notes and tech discussions), producing clean, structured entries that require minimal editing. For edge cases (contradictions, mixed topics, sparse notes), the system correctly flags issues but requires human judgment.

**Recommended deployment pattern:**
1. Automated ingestion of raw notes with LLM processing
2. Generated entries go to a "draft" folder or status
3. Human reviews and approves (or corrects) entries before moving to the permanent knowledge base
4. The model's own "Data Quality" notes serve as a review priority signal

Without human review, the system risks introducing inaccurate structured data into the knowledge base—particularly around dates, numbers, and decisions. The cost of a wrong knowledge-base entry (misleading future team members) exceeds the cost of a quick manual review.
