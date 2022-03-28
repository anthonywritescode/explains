import multiprocessing


def main() -> int:
    for _ in range(100000):
        with multiprocessing.Pool(2):
            pass
        print('.', end='', flush=True)
    print()


if __name__ == '__main__':
    raise SystemExit(main())
