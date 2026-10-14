# Report 0001: slow login

## For you

The brief asked for the login page to stop taking four seconds. It does now.
The page ran one database query for every row in the user's history, and the
history grows with every login, so the slowest users were the ones who had
been here longest. The query now runs once and the page takes under a second
for the heaviest account we have.

Nothing else moved. One test was added so the count of queries cannot climb
back without somebody noticing. Nothing is open and nothing needs a decision.

## Accepted

accepted:
in my words:

## For the director

### What changed

- `app/login.py`, the query left the loop.
- `tests/test_login.py`, one test for the count of queries.

### What was run

Nothing wrote to disk outside this repository.

### The check

```
formwork/fw check
GATE: green. 13 check(s), each shown to reject the wrong and accept the right.
```

### Git status

```
 M app/login.py
 M tests/test_login.py
```

### The three that matter

- **Done but not asked for.** Nothing.
- **Asked for but not done.** Nothing.
- **Wrong in the brief.** Nothing.
