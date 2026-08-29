# Actuals — how this now works

**The canonical log is the Google Doc "Alfred — Actuals Log"**
(`1Rg4s-c5nkGzX-GXwwGdektnP7Lql-_oY7Hu96MqG104`, folder `YNB x Claude`).
Find it by title search, never by a hard-coded ID.

**This directory holds each day's entry as it is written**, one file per day,
`YYYY-MM-DD.md`. Written on the last sweep of the day, committed, pushed.

## Why the split

Google Drive's `update_file` accepts only title and parentId — never content.
Appending to the Doc means reading it whole, rebuilding it whole, creating a
new file with the same title and parent, and trashing the old one, all in the
same pass or duplicates accumulate. That is a full-document rewrite every
single day, and every rewrite is a chance to lose the file.

So: the day's entry lands here first, where it is cheap, diffable and backed by
git. **The Doc is rebuilt on the Monday reconciliation pass**, folding in the
week's entries from this directory in date order. If a rebuild ever fails or
drops content, the entries here are the recovery source.

## The entry format, unchanged

```
DATE | PLANNED | ACTUAL | REASON | ADJUSTMENT
```

## The pattern rule, unchanged

Two occurrences is coincidence. Three is a pattern. Name a pattern at most
once, warmly, and always paired with a proposal to change the model — never a
demand to try harder. If reality keeps disagreeing with the ideal week in the
same place, the ideal week is what is wrong.
