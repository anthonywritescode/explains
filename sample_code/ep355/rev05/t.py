import concurrent.futures
import contextlib
import time
from typing import Generator


@contextlib.contextmanager
def time_it(what: str) -> Generator[None, None, None]:
    t0 = time.monotonic()
    try:
        yield
    finally:
        print(f'{what} took {time.monotonic() - t0}')


def do_work() -> int:
    with time_it('work'):
        x = 0
        time.sleep(1)
        # for _ in range(10_000_000):
        #     x += 1
        return x


def main() -> int:
    with time_it('main'):
        with concurrent.futures.ThreadPoolExecutor(1) as pool:
            futures = [pool.submit(do_work) for _ in range(20)]

            for future in concurrent.futures.as_completed(futures):
                print(f'got {future.result()}')

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
