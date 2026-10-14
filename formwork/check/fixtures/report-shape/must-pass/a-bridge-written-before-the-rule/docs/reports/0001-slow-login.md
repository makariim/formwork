# Report 0001: slow login

## For you

*Written by the director from the full report below, 14 Oct 2026. From the next brief on, the working session writes this part.*

The brief asked for the login page to stop taking four seconds. It does now.
The page ran one database query for every row in the user's history, and the
history grows with every login, so the slowest users were the ones who had
been here longest. The query now runs once and the page takes under a second
for the heaviest account we have.

Nothing else moved. One test was added so the count of queries cannot climb
back without somebody noticing. Nothing is open and nothing needs a decision.

## What changed

- `app/login.py`, the query left the loop.

## What was run

Nothing wrote to disk outside this repository.

## The check

Green, 12 checks.

## Git status

Nothing staged.

## The three that matter

Nothing, nothing, nothing.

## Accepted

accepted:
in my words:

