from mod import foo


def main() -> int:
    foo()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
