# case_2_normal
**Category:** normal
**Description:** Slack thread about WhatsApp API rate limits
**Prompt version:** v1

## Raw Input
```
slack convo from #dev channel. nadh: hey the whatsapp api rate limit is hitting us on pro tier. me: right now we're using the standard cloud api with no queue. nadh: can we add a message queue? me: yeah redis queue should work, we can throttle to 80msg/sec per WABA. nadh: ok spike it and let me know by tmr. also — the PII masking middleware is leaking phone numbers in logs. severity: high.
```

## Expected Behavior
Should capture the technical issue, proposed solution (Redis queue), flag the high-severity PII leak, and create action items.

## LLM Output


**Title:** WhatsApp API Rate Limit & PII Leak Issue – #dev Channel Discussion  

**Summary:**  
In the #dev Slack channel, nadh reported that the team is hitting WhatsApp API rate limits on the pro tier while using the standard Cloud API without any queuing mechanism. The proposed solution is to introduce a Redis‑backed message queue to throttle traffic to 80 messages per second per WABA, with a spike to be completed and reported by tomorrow. Additionally, the PII masking middleware is leaking phone numbers in logs, which has been flagged as a high‑severity issue.

**Key Points:**  
- **Current setup:** Standard WhatsApp Cloud API, no message queue in place.  
- **Problem:** WhatsApp API rate limit exceeded on the pro tier.  
- **Proposed fix:** Implement a Redis queue; throttle to **80 msg/sec per WABA**.  
- **Action item:** Spike the queue implementation and provide an update by tomorrow.  
- **Secondary issue:** PII masking middleware is leaking phone numbers in logs.  
- **Severity of PII leak:** **High**.
