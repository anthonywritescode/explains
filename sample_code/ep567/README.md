# [using memray to debug (and fix) a memory leak in krb5! (advanced)](https://youtu.be/bw5AHdZA7e4)

Today I show how I utilized memray to both find, debug, and ultimately fix a memory leak in krb5 -- sadly this was not the leak I was looking for though!

## Setup commands

```bash
git clone git@github.com:getsentry/sentry
# git clone https://github.com/getsentry/sentry
cd sentry
```

## Interactive examples

### Bash

Session 1:

```bash
python -m sentry run worker --queues counters-0 --concurrency 1 --max-tasks-per-child 1000000000
timeout --signal=SIGINT 10s memray run --quiet -m sentry run worker --queues counters-0 --concurrency 1 --max-tasks-per-child 1000000000

memray flamegraph --help
memray flamegraph --leaks <memray_bin_filename>
open <memray_flamegraph_html_filename>

PYTHONMALLOC=malloc timeout --signal=SIGINT 10s memray run --follow-fork --quiet -m sentry run worker --queues counters-0 --concurrency 1 --max-tasks-per-child 1000000000
memray flamegraph --leaks <memray_bin_filename>
open <memray_flamegraph_html_filename>

PYTHONMALLOC=malloc timeout --signal=SIGINT 20s memray run --follow-fork --quiet -m sentry run worker --queues counters-0 --concurrency 1 --max-tasks-per-child 1000000000
memray flamegraph --leaks <memray_bin_filename>
open <memray_flamegraph_html_filename>

PYTHONMALLOC=malloc memray run -m t
memray flamegraph --leaks <memray_bin_filename>
open <memray_flamegraph_html_filename>

PYTHONMALLOC=malloc memray run --native -m t
memray flamegraph <memray_bin_filename>
xdg-open <memray_flamegraph_html_filename>

gcc $(PKG_CONFIG_PATH=<broken_version> pkg-config kbr5-gssapi --cflags --libs) t.c
./a.out
leaks --atExit -- ./a.out

gcc $(PKG_CONFIG_PATH=<fixed_version> pkg-config kbr5-gssapi --cflags --libs) t.c
./a.out
leaks --atExit -- ./a.out
```

Session 2:

```bash
sentry exec t.py
```

Session 3:

```bash
htop --filter ' worker '
```
