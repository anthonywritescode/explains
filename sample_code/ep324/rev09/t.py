import tempfile


def main() -> int:
    with tempfile.TemporaryFile(mode='w') as tmpfile:
        tmpfile.write('foo')
        print(tmpfile.name)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
