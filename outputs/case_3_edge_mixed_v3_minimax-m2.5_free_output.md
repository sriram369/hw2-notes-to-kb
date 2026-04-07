# case_3_edge_mixed
**Category:** edge
**Description:** Mixed-topic brain dump (business + personal)
**Prompt version:** v3

## Raw Input
```
random things on my mind today: the omagent pricing tiers might need adjusting — enterprise at 25k feels low. also need to fix the docker compose file it keeps failing on m1. oh and reminder: call dentist at 3pm wednesday. the new gemma model from google is surprisingly good for tool use, should test it in sri-workflow. my phone battery dying too fast.
```

## Expected Behavior
Should NOT merge everything into one entry. Good output: splits into separate entries (business/tech vs personal), or flags personal items as out of scope.

## LLM Output
---
title: Mixed Notes - Pricing Docker AI Model
date: 2025-01-22
type: brainstorm
tags: [pricing, docker, ai-models, omagent, gemma]
---

# [[Mixed Notes - Pricing Docker AI Model]]

## Summary
Collection of unrelated notes covering Omagent pricing review, Docker compose issues on M1, a new Google Gemma model for testing, and personal reminders.

## Key Details
- **Omagent pricing**: Enterprise tier at 25k feels low, may need adjusting
- **Docker**: Docker compose file keeps failing on M1 (Apple Silicon) - needs fixing
- **AI Model**: New Google Gemma model is "surprisingly good for tool use" - want to test in sri-workflow
- **Personal**: Call dentist at 3pm Wednesday

## Action Items
- [ ] Review Omagent enterprise pricing tiers (assigned to: self, deadline: TBD)
- [ ] Fix docker compose file for M1 compatibility (assigned to: self, deadline: TBD)
- [ ] Test Gemma model in sri-workflow (assigned to: self, deadline: TBD)

## Notes on Data Quality
**MIXED TOPICS DETECTED**: These notes contain unrelated items that should be split:
- Business/technical items: Omagent pricing, Docker issue, Gemma model testing
- Personal item: Dentist call (out of scope for work wiki)
- Vague item: Phone battery dying (no action specified, out of scope)

**CONFLICTS/AMBIGUITIES**:
- "Wednesday" has no year/month - needs specific date
- No context for "sri-workflow" - unclear what this refers to
- "25k" - unclear if monthly, annual, or one-time pricing

## Related
- [[Omagent Pricing]]
- [[Docker Setup]]
- [[Gemma Model]]
- [[sri-workflow]] (unconfirmed - name may be incorrect)
