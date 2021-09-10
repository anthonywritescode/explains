import subprocess
import tempfile


def main() -> int:
    with tempfile.NamedTemporaryFile(mode='w') as tmpfile:
        tmpfile.write('foo\n')
        tmpfile.flush()
        print(tmpfile.name)
        subprocess.check_call(('cat', tmpfile.name))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
