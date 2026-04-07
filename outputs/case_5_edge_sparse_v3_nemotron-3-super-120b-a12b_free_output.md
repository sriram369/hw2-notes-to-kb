# case_5_edge_sparse
**Category:** edge
**Description:** Very sparse/cryptic notes
**Prompt version:** v3

## Raw Input
```
api — timeout
fix by 5pm
nadh said no
wssdk — ??
```

## Expected Behavior
Should recognize insufficient context, list what can be partially extracted, and ask for clarification rather than hallucinating details.

## LLM Output
We need to parse notes: "api — timeout", "fix by 5pm", "nadh said no", "wssdk — ??". Likely meeting notes about API timeout, need to fix by 5pm, nadh said no (maybe to something), wssdk — ?? (unknown). We need to produce structured entry with title, date, type, tags. No date given, so we need to infer? The instruction: preserve names, dates, deadlines exactly as stated. No date given in notes. So we cannot invent date. We could leave date blank? But format requires date: YYYY-MM-DD. We must not invent. If missing, we should say insufficient info? The instruction: If notes are too sparse or cryptic to produce a meaningful entry, say so clearly and list what information is missing. So we should note missing date, missing context. So we should output that we cannot produce meaningful entry due to missing date, unclear context. Provide what's missing: date, clarification of what nadh said no to, what wssdk ?? means, etc. So output should indicate inability. Probably we should still output the frontmatter but with placeholders? Better to say cannot produce. The instruction: "If the notes are too sparse or cryptic to produce a meaningful entry, say so clearly and list what information is missing." So we should output a message, not the structured entry? Likely we should output a note saying insufficient info. But the format requires the frontmatter etc. However we can still output the frontmatter with unknown values? But that would be inventing. Safer to output a plain text saying insufficient info. But the user explicitly says output MUST follow this format exactly. So we must produce the markdown with frontmatter etc. But we can fill missing fields with placeholders like "unknown" or blank? That might be considered inventing? The instruction: NEVER invent or hallucinate details not present. So we cannot fill date with a fake date. We could leave date empty? But format expects YYYY-MM-DD. Could we put "null"? That's not a date. Might be considered not following format. Perhaps we can note in the entry that date is missing, and put something like "date: 0000-00-00"? That's invented. Better to follow instruction: If too sparse, say so clearly and list what information is missing. So we can produce an entry where the summary says insufficient info, and in Notes on Data Quality we list missing info. The frontmatter still needs a date; we could set date to the date of the note? Not given. Could we use today's date? That would be inventing. Not allowed. So maybe we can omit date? But format requires it. Perhaps we can put "date: unknown". That's not a date but it's not inventing a specific false date; it's indicating unknown. Might be acceptable. The instruction: preserve names, dates, and deadlines exactly as stated. If not stated, we should not invent. So we can put "date: unknown". That is not inventing a specific date, it's marking unknown. I think that's okay. Similarly, we can set title to something generic like "API Timeout Discussion". But that might be inventing. However we can derive title from notes: "api — timeout". So title could be "API Timeout". That's derived from notes, not invented. So we can set title: "API Timeout". Type: meeting-notes (makes sense). Tags: [api, timeout, wssdk, nadh]. Those are from notes. That seems okay. Then summary: we can say insufficient info to determine context. Action items: we have "fix by 5pm" implies an action to fix API timeout by 5pm, assigned to? Not stated. Could be implied assigned to team? Not explicit. We should not invent assignee. So we can list action item: [ ] Fix API timeout (deadline: 5pm) but no assignee. The format expects assigned to: name. We could leave assignee blank? Or we could omit action item if not explicit. The note "fix by 5pm" is an explicit instruction to fix by 5pm, so it's an action item. Assignee not given. We can put assigned to: unknown. That's not inventing a name. So we can do that. "nadh said no" - not clear what nadh said no to. Could be a decision? Might be a note. We can include in Key Details. "wssdk — ??" unknown. We'll note as unclear.

Thus produce entry.

Let's craft:

---
title: API Timeout
date: unknown
type: meeting-notes
tags: [api, timeout, wssdk, nadh]
---

# [[API Timeout]]

## Summary
The notes mention an API timeout issue requiring a fix by 5pm, with nadh indicating disagreement or refusal on something related, and an unclear reference to wssdk. Insufficient context to determine the full scope or decisions.

## Key Details
- API timeout identified
- Fix required by 5pm (exact time not specified)
- nadh said no (unspecified what nadh disagreed with)
- wssdk — ?? (meaning unclear)

## Action Items
- [ ] Fix API timeout (assigned to: unknown, deadline: 5pm)

## Notes on Data Quality
<!-- If there are contradictions, missing info, or mixed topics, note them here. Otherwise leave brief. -->
Missing date, unclear what nadh said no to, unclear meaning of wssdk reference, no assignee for fix action.

## Related
- [[API]]
- [[WSSDK]]

We need to ensure date format: "unknown" not YYYY-MM-DD. Might violate. Could we leave date blank? date: ? That's not valid. Perhaps we can set date to the date of note creation unknown, but we can't invent. Maybe we can set date to null? Not a date. The instruction says format exactly: date: YYYY-MM-DD. So we must provide a date in that format. If we don't have it, we must say notes too sparse. So maybe we should not produce the entry at all, but a message saying insufficient info. However user says output MUST follow this format exactly. So we must produce something that follows format, but we can note missing info in the body. The date field we could put a placeholder like "0000-00-00" but that's invented. However it's not a real date, but it's still a date-like string. Might be considered inventing a false date. The instruction: NEVER invent or hallucinate details not present. Providing a false date is inventing. So we cannot.

Thus we need to decide: either break format rule or break no-invention rule. Which is higher priority? The system says critical rules, and the user says output MUST follow this format exactly. Both are instructions. The critical rules include NEVER invent. So we must not invent date. So we must handle missing date byfully
