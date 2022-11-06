import multiprocessing


glob = 1


def x(y: int) -> int:
    return glob + y


def main() -> int:
    global glob

    glob = 2

    print('fork')
    with multiprocessing.get_context('fork').Pool(2) as p:
        print(list(p.map(x, (1, 2, 3))))

    print('spawn')
    with multiprocessing.get_context('spawn').Pool(2) as p:
        print(list(p.map(x, (1, 2, 3))))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
