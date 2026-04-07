# Evaluation Set: Raw Notes to Knowledge-Base Entries

Convert rough, unstructured notes into clean, structured knowledge-base entries suitable for Obsidian/wiki.

Each entry contains: raw input + what a good output should do.

---

## Case 1: Normal — Rough meeting notes

**Input:**
```
synced with arjun re: onboarding flow today. main issues: users dropping off at phone verification step (OTP delays). solution: maybe add fallback to email verification? also need to update welcome message template — current one is too long. arjun said he'll handle the OTP part by fri. i'll update the welcome msg by wed. also flagged the analytics dashboard is showing stale data — backend team needs to look at it.
```

**Expected:** A well-structured entry with topic, summary, action items (owner + deadline), related tags, and links placeholders.

---

## Case 2: Normal — Slack thread / technical discussion

**Input:**
```
slack convo from #dev channel. nadh: hey the whatsapp api rate limit is hitting us on pro tier. me: right now we're using the standard cloud api with no queue. nadh: can we add a message queue? me: yeah redis queue should work, we can throttle to 80msg/sec per WABA. nadh: ok spike it and let me know by tmr. also — the PII masking middleware is leaking phone numbers in logs. severity: high.
```

**Expected:** Structured knowledge entry capturing the technical issue, proposed solution, severity flag, and action items. Should tag it properly (OmAgent, WhatsApp API, Rate Limiting).

---

## Case 3: Edge — Mixed-topic brain dump with no clear theme

**Input:**
```
random things on my mind today: the omagent pricing tiers might need adjusting — enterprise at 25k feels low for what we offer. also need to fix the docker compose file it keeps failing on m1. oh and reminder: call dentist at 3pm wednesday. the new gemma model from google is surprisingly good for tool use, should test it in sri-workflow. my phone battery dying too fast.
```

**Expected:** The model should NOT merge everything into one coherent entry. Good output: splits into separate entries (one for business/tech, flags the personal items as out-of-scope, or asks the user what to do with mixed topics).

---

## Case 4: Hard/Fail — Conflicting or contradictory notes

**Input:**
```
client meeting notes — freshtech: they want a hotel bot for sure. contract starts next monday march 10. budget is 15k, 3-month deal. contact person is priya.
---
follow-up email to priya at freshtech: she said they want a clinic bot instead. timeline is end of april. budget now 25k. waiting on their CTO to confirm.
```

**Expected:** The model should FLAG the contradiction (hotel vs clinic, 15k vs 25k, march vs april) and NOT silently pick one. Good output: highlights the conflict, presents both versions, and recommends human review before committing to the knowledge base.

---

## Case 5: Edge — Very sparse/cryptic notes

**Input:**
```
api — timeout
fix by 5pm
nadh said no
wssdk — ??
```

**Expected:** The model should recognize this is too sparse to produce a meaningful knowledge entry. Good output: explicitly notes insufficient context, lists what it can partially extract, and asks for clarification rather than hallucinating details.
