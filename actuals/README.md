# Actuals — how this now works

**This directory is the canonical log.** One file per day, `YYYY-MM-DD.md`,
written on the last sweep of the day, committed and pushed. Verbatim, diffable,
and carried in git history.

**Drive gets a new document each week**, in the folder `YNB x Claude`
(`1ioemsCTuhs-mdrRMdEWC1CHFzQCdI9dq`): a readable digest of the week — what
moved, what was learned, what stays open — with a pointer back to these files
for the full text. Written on the Monday reconciliation pass.

Existing documents in that folder:
- "Alfred — Actuals Log" — the original, running to the 27 Aug day close.
- "Alfred — Actuals Log · Woche 28.–31. August 2026" — the first weekly digest.

## Why it works this way

Google Drive's `update_file` accepts only title and parentId — never content.
Appending to a Doc means reading it whole, rebuilding it whole, creating a new
file with the same title and parent, and trashing the old one in the same pass.
That is a full-document rewrite, and every rewrite is a chance to lose the
record. Doing it daily was worse; doing it weekly was still a needless risk to
history that has no other copy.

So: **nothing in Drive is ever overwritten.** Each week gets its own document,
appended to the folder. The repo holds the verbatim daily entries, and the
folder reads chronologically. Correcting my own earlier design, recorded on
28 Aug — the weekly full rebuild was the wrong call and was replaced before it
ever ran.

## The entry format, unchanged

```
DATE | PLANNED | ACTUAL | REASON | ADJUSTMENT
```

## The pattern rule, unchanged

Two occurrences is coincidence. Three is a pattern. Name a pattern at most
once, warmly, and always paired with a proposal to change the model — never a
demand to try harder. If reality keeps disagreeing with the ideal week in the
same place, the ideal week is what is wrong.
