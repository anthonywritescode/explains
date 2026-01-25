import psutil
import subprocess
import time


proc = subprocess.Popen(
    ('getsentry', 'configoptions', 'sync'),
    stdin=subprocess.PIPE,
    # stderr=subprocess.DEVNULL,
)
time.sleep(5)
psutil_proc = psutil.Process(proc.pid)
rss = psutil_proc.memory_info().rss
print(f'rss: {rss}')
proc.terminate()
proc.wait(timeout=1)

raise SystemExit(rss > 300_000_000)
