import gc
import multiprocessing
import time

import asyncio
import ctypes
import ssl


def square(x: int) -> int:
    gc.collect()
    time.sleep(15)
    return x ** x


def main() -> int:
    print('starting')
    gc.freeze()
    with multiprocessing.Pool(4) as p:
        list(p.map(square, range(4)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
