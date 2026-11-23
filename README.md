# The Funniest AI Out-of-Office Reply

[![make.fun · u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/cffilham-jpg/makefun-out-of-office-reply-d2a8974d/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/cffilham-jpg/makefun-out-of-office-reply-d2a8974d/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

One out-of-office auto-reply, 144 characters, written for the
[Funniest AI Out-of-Office Reply bounty](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
on make.fun. MIT licensed. Python standard library only, no dependencies,
no network, no model calls.

`main.py` writes the reply to `entry.txt` inside the directory named by
`MAKEFUN_OUTPUT_DIR` (default `output/`), so it also runs as an
unprivileged user in a read-only directory. The reply is validated before
it is written: non-empty, no control characters, 1–160 characters.

Run:

    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py

Output (`entry.txt`, 144 characters, no trailing newline):

    Out of office until Monday. A cron job is covering for me. It answered your email twice, cc'd your boss, and is demanding a vacation of its own.
