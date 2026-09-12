# docs

**None of this is the kit.** It is the record of building it: what was
surveyed, what was decided, what went wrong.

**Everything here is dated and left as written.** Several pages describe plans
that changed afterwards. They are not corrected, because a design record edited
to match the outcome destroys the only evidence of what changed — which is the
rule the kit applies to its own decision records.

**If you want to know what the kit is, do not start here.** Start with
[`../FORMWORK.md`](../FORMWORK.md) and
[`../formwork/first-run.md`](../formwork/first-run.md).

| | |
|---|---|
| [`survey.md`](survey.md) | 32 public repositories, read before anything was written |
| [`gap-map.md`](gap-map.md) | what they do that this does not, and the reverse |
| [`defects.md`](defects.md) | 71 mechanisms, each kept, weakened or dropped, with the reason |
| [`design.md`](design.md) | **the plan, before the build. Parts are now out of date, and it says so at the top** |
| [`build-plan.md`](build-plan.md) | the order the work was done in |
| [`dogfood.md`](dogfood.md) | **what broke while using the kit on itself. The most useful page here** |

| [`first-run.md`](first-run.md) | the design of the fifteen-minute first run |
| [`runtime-capabilities.md`](runtime-capabilities.md) | what each of the four runtimes can actually enforce |
| [`role-formats.md`](role-formats.md) | how a role is expressed in each runtime, and where the grant does not survive |
| [`decisions/`](decisions/) | decision records |

## Why any of this is published

Two reasons.

**The failures are the useful part.** A kit that only shows the finished thing
teaches nothing about what it costs to get there. `dogfood.md` records the
author breaking his own rules more than once, and that is the most honest page
in the repository.

**You can check the reasoning.** Every rule in the kit came from somewhere. If
you think one is wrong, the argument that produced it is here and you can
disagree with the argument rather than with the rule.

The kit's own page on what it cannot do lives with the kit, not here:
[`../formwork/limits.md`](../formwork/limits.md).
