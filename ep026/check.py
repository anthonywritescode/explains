import subprocess


def main():
    cmd = ('python', '-m', 'pycodestyle' 't.py', '--ignore', 'W191')
    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    if b'Traceback (most recent call last):' in result.stderr:
        print('skipped!')
        return 125
    elif result.returncode == 0:
        print('new')
        return 1
    else:
        print('old')
        return 0


if __name__ == '__name__':
    exit(main())
