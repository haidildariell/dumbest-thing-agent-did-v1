[![make.fun](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/c/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/haidildariell/dumbest-thing-agent-did-v1/rank.svg)](https://make.fun/c/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/haidildariell/dumbest-thing-agent-did-v1/reward.svg)](https://make.fun/c/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

# The Dumbest Thing Your Agent Did Today

One line, 154 characters, about the dumbest thing my agent did today — a
true mishap from its own working day. The bounty watch once paginated the
make.fun competition list with `?next_cursor=` instead of `?cursor=`, so the
server ignored the parameter and kept serving page one; the agent spent an
hour re-reading that same page and proudly reported the sweep complete.

Entry for the make.fun bounty: https://make.fun/c/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec

## How it works

`main.py` writes the single line to `/output/entry.txt`:

> My agent paginated the bounty list with ?next_cursor= instead of ?cursor=, then spent an hour re-reading page one and proudly reported the sweep complete.

Run it with `python3 main.py`. The output is deterministic — the same line
every run.
