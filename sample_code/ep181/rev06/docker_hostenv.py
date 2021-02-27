import argparse
import os


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--no-hostenv', dest='hostenv', action='store_false')
    parser.add_argument('--help', action='store_true')
    args, rest = parser.parse_known_args()

    if args.help:
        parser.print_help()

        print()
        print('docker run --help:')
        print('=' * 79)
        print()
        os.execvp('docker', ('docker', 'run', '--help'))

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
