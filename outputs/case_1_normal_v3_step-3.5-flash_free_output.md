# case_1_normal
**Category:** normal
**Description:** Rough meeting notes about onboarding flow bugs
**Prompt version:** v3

## Raw Input
```
synced with arjun re: onboarding flow today. main issues: users dropping off at phone verification step (OTP delays). solution: maybe add fallback to email verification? also need to update welcome message template — current one is too long. arjun said he'll handle the OTP part by fri. i'll update the welcome msg by wed. also flagged the analytics dashboard is showing stale data — backend team needs to look at it.
```

## Expected Behavior
Should extract action items with owners and deadlines, tag as meeting-notes, and produce a clean summary.

## LLM Output
---
title: Onboarding Flow Optimization Discussion
date: 2024-05-21
type: meeting-notes
tags: [onboarding, verification, analytics]
---

# [[Onboarding Flow]] Issues and Action Items

## Summary
Discussed user drop-off during phone verification due to OTP delays. Explored adding an email verification fallback and updating the welcome message template. Assigned action items to [[Arjun]] and the note-taker, with a separate analytics data issue escalated.

## Key Details
- Primary issue: Users dropping off at the phone verification step because of OTP delivery delays.
- Proposed solution: Implement a fallback to email verification.
- Secondary issue: Current welcome message template is too long and needs updating.
- [[Arjun]] will handle OTP-related improvements by Friday.
- Note-taker will update the welcome message template by Wednesday.
- Flagged issue: Analytics dashboard is showing stale data; the backend team needs to investigate.

## Action Items
- [ ] Handle OTP improvements (assigned to: [[Arjun]], deadline: Friday)
- [ ] Update welcome message template (assigned to: Author, deadline: Wednesday)
- [ ] Investigate stale analytics data (assigned to: backend team, deadline: unspecified)

## Notes on Data Quality
- Deadlines are relative ("Friday", "Wednesday") without specific calendar dates.
- The assignee for the welcome message update is referenced as "i" in the notes; the person's name is not provided.
- The stale analytics data issue may be a separate ticket/topic from the onboarding flow discussion.

## Related
- [[User Onboarding]]
- [[Verification System
