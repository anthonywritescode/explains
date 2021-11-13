import concurrent.futures
import time


with concurrent.futures.ThreadPoolExecutor(4) as pool:
    futures = [pool.submit(time.sleep, 10) for _ in range(10)]
    list(concurrent.futures.as_completed(futures))
