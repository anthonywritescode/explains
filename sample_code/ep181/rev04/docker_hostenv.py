import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-hostenv', dest='hostenv', action='store_false')
    args, rest = parser.parse_known_args()

    if args.hostenv:
        cmd = (
            'docker', 'run',
            '-e', f'HOST_USER={os.getuid()}',
            '-e', f'HOST_GROUP={os.getgid()}',
            *rest,
        )
    else:
        cmd = ('docker', 'run', *rest)

    os.execvp(cmd[0], cmd)


if __name__ == '__main__':
    exit(main())
