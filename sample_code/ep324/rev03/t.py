import tempfile


def main() -> int:
    with tempfile.TemporaryDirectory(suffix='wat') as tmpdir:
        print(tmpdir)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
