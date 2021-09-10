import tempfile
import shutil


def main() -> int:
    with tempfile.TemporaryDirectory() as tmpdir:
        print(tmpdir)
        shutil.rmtree(tmpdir)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
