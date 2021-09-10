import tempfile


def main() -> int:
    with tempfile.TemporaryFile() as tmpfile:
        print(tmpfile)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
