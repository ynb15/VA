# Alfred — YNB Command Center

A self-maintaining command centre for Yannick Noah Bernard. An hourly routine sweeps
calendar, email and Drive, rebuilds a single dashboard, and stays quiet unless
something changed.

**Board:** https://claude.ai/code/artifact/36c602cc-f6a8-46a7-89c3-937111cd431d
(stable URL — every sweep republishes to it)

## The three durable stores

| Store | Where | Purpose |
|---|---|---|
| Operating manual | `OPERATING-MANUAL.md`, pasted as the trigger prompt | Every correction ever given. The most important artifact here. |
| Dashboard | the artifact URL above; source in `dashboard/` | Current state |
| Actuals log | Drive → `YNB x Claude` → **Alfred — Actuals Log** | Planned vs. what really happened |

The actuals log is deliberately **not** in `[Alfred] Inbox` — the sweep empties that
folder every hour and would delete its own memory.

## Wiring

- **Note-back folder:** `[Alfred] Inbox` in My Drive — `1BTFS3WpV2XbTMDz0knlSMOPjNOziRzO9`
  Drop a note in. Next sweep reads it, acts on it, deletes it.
- **Trigger:** `Alfred — hourly sweep` (`trig_01FnmMyeG9ynGwbzNxwnSQLu`)
  Cron `0 0-3,12-23 * * *` UTC = hourly 07:00–22:00 Austin, bound to one persistent session.
- **Calendars:** `ynb@yannick-noah.com` (business) · `yannicknbernard@gmail.com` (private)
- **Permissions:** `.claude/settings.json` and `.claude/settings.local.json`.
  Calendar and Drive writes pre-approved. **All outbound messaging denied** —
  drafting is fine, sending is not.

## Known gap

The Routine was created through the API, which cannot attach MCP connectors for this
organization. It fires into this persistent session, which does hold Gmail, Calendar
and Drive — but if a fired sweep reports it has no connector tools, recreate the
Routine from the claude.ai Routines UI (paste `OPERATING-MANUAL.md` as the prompt)
and delete `trig_01FnmMyeG9ynGwbzNxwnSQLu`.

## Dashboard notes

- Single-theme dark, committed on purpose. No light variant unless asked.
- Cross-tab state: every checkbox carries `data-item`; identical keys sync on change,
  recompute every progress bar and stat, and persist to `localStorage`.
- Committed hours are a **union of intervals**, so overlapping events count once.
- The strip under each day bar is the real Google Calendar event colours, in order
  through the day. Graphite is lightened to `#8E9199` because true Graphite
  disappears on a black ground.
- Proposal buttons are Google Calendar template links. Nothing lands without a press.
- Timestamps render in `America/Chicago`, never the viewer's timezone.

## The one thing that matters

The manual grows. When Alfred gets something wrong, the correction goes into
**THINGS ALREADY SETTLED** in `OPERATING-MANUAL.md` and into the live trigger prompt —
not just into today's board. A correction that only fixes today resurfaces next week.
