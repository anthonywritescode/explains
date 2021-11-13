import concurrent.futures


def do_work() -> int:
    x = 0
    for _ in range(1_000_000):
        x += 1
    return x


def main() -> int:
    with concurrent.futures.ThreadPoolExecutor(4) as pool:
        futures = [pool.submit(do_work) for _ in range(20)]

        for future in concurrent.futures.as_completed(futures):
            print(f'got {future.result()}')

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
