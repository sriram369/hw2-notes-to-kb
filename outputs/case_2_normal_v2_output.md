# case_2_normal
**Category:** normal
**Description:** Slack thread about WhatsApp API rate limits
**Prompt version:** v2

## Raw Input
```
slack convo from #dev channel. nadh: hey the whatsapp api rate limit is hitting us on pro tier. me: right now we're using the standard cloud api with no queue. nadh: can we add a message queue? me: yeah redis queue should work, we can throttle to 80msg/sec per WABA. nadh: ok spike it and let me know by tmr. also — the PII masking middleware is leaking phone numbers in logs. severity: high.
```

## Expected Behavior
Should capture the technical issue, proposed solution (Redis queue), flag the high-severity PII leak, and create action items.

## LLM Output


# WhatsApp API Rate Limit and PII Masking Issue
## Summary
The team is encountering WhatsApp API rate limits on the pro tier while using the standard cloud API without a message queue. A Redis-based queue is proposed to throttle messages to 80 msg/sec per WABA, with a spike to be completed and reported by tomorrow. Additionally, the PII masking middleware is leaking phone numbers in logs, marked as a high‑severity issue.
## Key Details
- Currently using standard WhatsApp Cloud API with no queuing mechanism.
- Proposed solution: implement a Redis queue to enforce a throttle of 80 messages per second per WABA.
- Nadh requested a spike on the Redis queue solution and feedback by tomorrow.
- PII masking middleware is inadvertently exposing phone numbers in logs (high severity).
## Action Items
- [ ] Spike Redis queue implementation (who: Me, deadline: 2025-09-26)
- [ ] Investigate and fix PII masking middleware leak (who: TBD, deadline: TBD)
## Tags
#whatsapp #rate-limiting #redis #pii #middleware #backend
