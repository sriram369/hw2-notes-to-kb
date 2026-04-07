# case_2_normal
**Category:** normal
**Description:** Slack thread about WhatsApp API rate limits
**Prompt version:** v3

## Raw Input
```
slack convo from #dev channel. nadh: hey the whatsapp api rate limit is hitting us on pro tier. me: right now we're using the standard cloud api with no queue. nadh: can we add a message queue? me: yeah redis queue should work, we can throttle to 80msg/sec per WABA. nadh: ok spike it and let me know by tmr. also — the PII masking middleware is leaking phone numbers in logs. severity: high.
```

## Expected Behavior
Should capture the technical issue, proposed solution (Redis queue), flag the high-severity PII leak, and create action items.

## LLM Output
---
title: WhatsApp API Rate Limit and PII Masking Middleware Issue
date: 2025-09-24
type: tech-note
tags: [WhatsApp, API, Redis, PII, middleware]
---

# [[WhatsApp API Rate Limit and PII Masking Middleware Issue]]

## Summary
The team discussed hitting WhatsApp API rate limits on the pro tier due to using the standard cloud API without a queue. A Redis-based message queue was proposed to throttle to 80 messages/sec per WABA. Additionally, the PII masking middleware was found to be leaking phone numbers in logs, marked as high severity.

## Key Details
- Current setup: standard cloud WhatsApp API, no queue in use
- Proposed solution: add Redis queue to throttle messages to 80msg/sec per WABA
- Nadh requested a spike on the queue solution with feedback by tomorrow
- PII masking middleware is leaking phone numbers in logs (severity: high)

## Action Items
- [ ] Spike Redis queue solution for WhatsApp API throttling (assigned to: ?, deadline: tomorrow)
- [ ] Investigate and fix PII masking middleware leaking phone numbers in logs (assigned to: ?, deadline: ?)

## Notes on Data Quality
<!-- If there are contradictions, missing info, or mixed topics, note them here. Otherwise leave brief. -->
Date not explicitly stated in notes; assumed today's date for format compliance. Assignees for action items are not specified in the conversation.

## Related
- [[WhatsApp API]]
- [[Redis queue]]
- [[PII masking middleware]]
