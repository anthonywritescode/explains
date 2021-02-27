# import argparse
import os
import sys


def main():
    # parser = argparse.ArgumentParser()
    cmd = (
        'docker', 'run',
        '-e', f'HOST_USER={os.getuid()}',
        '-e', f'HOST_GROUP={os.getgid()}',
        *sys.argv[1:],
    )
    os.execvp(cmd[0], cmd)


if __name__ == '__main__':
    exit(main())
