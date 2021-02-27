import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-hostenv', action='store_true')
    args, rest = parser.parse_known_args()

    cmd = (
        'docker', 'run',
        '-e', f'HOST_USER={os.getuid()}',
        '-e', f'HOST_GROUP={os.getgid()}',
        *rest,
    )
    os.execvp(cmd[0], cmd)


if __name__ == '__main__':
    exit(main())
