import tempfile


def main() -> int:
    with tempfile.TemporaryDirectory() as tmpdir:
        print(tmpdir)
        breakpoint()
        pass

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
