# HW2 — GenAI Workflow: Notes to Knowledge-Base Entries

**Name:** OM  
**Course:** [Course Name]  
**Unlisted Video Walkthrough:** [to be added]

## Overview

This prototype converts raw, unstructured notes (meeting notes, Slack snippets, brain-dumps) into structured, Obsidian-compatible knowledge-base entries. It uses an LLM to extract topics, summarize content, identify action items, tag entries, and produce clean Markdown with YAML frontmatter.

## Files

| File | Description |
|---|---|
| `app.py` | Python CLI script that calls the LLM via OpenRouter |
| `prompts.md` | Initial prompt → Revision 1 → Revision 2 with change notes |
| `eval_set.md` | 5 test cases with expected behaviors |
| `report.md` | Analysis report with baseline vs. final comparison |

## Setup

```bash
# Install dependencies
pip install openai

# Set your API key (export or .env)
export OPENROUTER_API_KEY="your-key-here"

# Run
python app.py
```

## Chosen Business Workflow

**Workflow:** Turning messy notes into structured knowledge-base answers

### The Problem

Engineers and founders constantly dump raw, unstructured notes (meeting notes, Slack threads, Slack DMs, quick thoughts) but rarely take the time to organize them. This creates knowledge silos and lost context.

### The User

A small technical team lead or founder who needs to quickly capture decisions, action items, and technical notes from meetings or Slack conversations.

### Input

Raw text notes pasted or piped from stdin, Slack exports, or quick voice-to-text.

### Output

A structured Markdown knowledge-base entry with YAML frontmatter, summary, action items, tags, and proper Obsidian-style wikilinks.

### Why This Matters

Instead of losing context or manually formatting notes, teams can automatically convert raw input into search-ready, well-organized knowledge base articles.
