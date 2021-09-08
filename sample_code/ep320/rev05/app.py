from mod import foo


def main() -> int:
    for _ in range(5):
        foo()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
