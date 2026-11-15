---
status: open
---

**Size:** checkpoint

Make search results load faster on the dashboard.

## Goal
Search is slow on large accounts and people give up.

## Scope
The search endpoint, its query builder, and the result cache.
Out of scope: the indexer, the admin screen.

## Must not happen
No change to the index format.
No new dependency.

## Done when
p95 under 400 ms on the large fixture account.
The cache is invalidated on every write.

## Checked by
formwork check, plus the timing script.

## The report must contain
The timings before and after.
