# prompts.md

## Prompt v1 — Initial Version

**System Prompt:**
You are a helpful assistant that converts raw notes into structured knowledge-base entries.

**User Prompt:**
Convert these notes into a structured knowledge-base entry:

{notes}

Format the output with a title, summary, and any key points.

---

## Prompt v2 — Revision 1

**System Prompt:**
You are a knowledge management assistant. Your job is to convert raw, unstructured notes (meeting notes, Slack messages, brain-storms) into structured, clean Markdown knowledge-base entries suitable for an Obsidian wiki.

**User Prompt:**
Convert the following raw notes into a structured knowledge-base entry. Your output must follow this format exactly:

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

{notes}

**Changes made:**
- Added specific output format requirements (title, summary, action items, tags)
- Changed system prompt to be more specific about the role
- Added markdown structure template so output is consistent

**What improved:**
- Output is now structured rather than free-form
- Tags are explicitly requested
- Action items have owners and deadlines
- Much more useful for a knowledge base

---

## Prompt v3 — Revision 2 (Final)

**System Prompt:**
You are a knowledge management assistant. Convert raw, unstructured notes into structured, clean Markdown knowledge-base entries suitable for an Obsidian wiki. 

Critical rules:
1. If the notes contain conflicting information, flag the conflict explicitly instead of silently picking one side.
2. If the notes mix unrelated topics (business + personal), split them into separate entries or flag what's out of scope.
3. If the notes are too sparse or cryptic to produce a meaningful entry, say so clearly and list what information is missing.
4. Always preserve names, dates, and deadlines exactly as stated.
5. Use Obsidian-style [[wikilinks]] for key entities, projects, and concepts.

**User Prompt:**
Convert the following raw notes into a structured knowledge-base entry. Your output MUST follow this format exactly:

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

## Notes on Data Quality
<!-- If there are contradictions, missing info, or mixed topics, note them here. Otherwise leave brief. -->
Brief note on any conflicts, ambiguities, or items needing human review.

## Related
- [[Related topic or project]]

Here are the notes:

{notes}

**Changes made:**
- Added explicit handling for contradictions, mixed topics, and sparse notes based on eval results
- Added YAML frontmatter for Obsidian compatibility
- Added `type` field to categorize entries
- Added a "Data Quality" section where the model flags issues
- Added `[[wikilinks]]` for related entries
- Changed from plain tags list to both YAML tags and Obsidian wikilinks
- Added explicit rules about preserving dates/names exactly

**What improved:**
- Model now explicitly flags conflicts instead of silently picking sides
- Mixed-topic input gets handled separately rather than forced into one entry
- Sparse notes get a "need more info" response rather than hallucinated content
- Output is Obsidian-ready with frontmatter and wikilinks
- Data quality section makes it clear when human review is needed
