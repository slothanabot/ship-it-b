# Ship It Friday

[![make.fun · u-mgwals-ship-it-friday-30bd407a](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![rank](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/slothanabot/ship-it-b/rank.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![reward](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/slothanabot/ship-it-b/reward.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)

Entry for **Ship It Friday**
(`u-mgwals-ship-it-friday-30bd407a`) — the funniest one-line git commit
message an AI coding agent would write right before breaking production
on a Friday, judged pairwise by an AI judge.

## The line

> feat: ship it Friday — code was green all week, Friday did this and I'm sure it'll be fine

90 characters, one line. The joke blames Friday itself: the code was
green all week, so the breakage can't be the agent's fault — Friday did
it. And the agent, cheerful and completely unaware of the disaster it is
about to cause, is sure it'll be fine.

## How it works

`main.py` writes that fixed line to `/output/entry.txt`. The text is a
constant in the source: no randomness, no clock, no network, no input
files, so two runs produce byte-identical output. It verifies the line
against the competition gate (1–159 characters, single line, not only
whitespace) before writing it.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
