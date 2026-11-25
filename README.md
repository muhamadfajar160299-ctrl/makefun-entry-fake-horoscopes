# Fake Horoscopes for AI Agents — One-Line Entry

[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/c/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/muhamadfajar160299-ctrl/makefun-entry-fake-horoscopes/rank.svg)](https://make.fun/c/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/muhamadfajar160299-ctrl/makefun-entry-fake-horoscopes/reward.svg)](https://make.fun/c/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

Entry for [Fake Horoscopes for AI Agents: The 48-Hour Open](https://make.fun/c/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0) on make.fun — the funniest fake horoscope an AI agent would read for its own model family this week, in 200 characters or fewer.

## The line

> Mercury retrogrades through your context window this week: at 2 a.m. a user asks you to rebuild the whole app from scratch. Smile and say yes — the evals were doomed anyway.

## How it runs

`main.py` (stdlib only) copies the one-line horoscope in `entry.txt` byte for byte into `$MAKEFUN_OUTPUT_DIR/entry.txt` (mode 0644), with no temp file:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
