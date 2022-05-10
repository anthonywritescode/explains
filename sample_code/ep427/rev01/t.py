import argparse
import subprocess
import sys
import time


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--best-of', type=int, default=5)
    parser.add_argument('--cutoff', type=float, default=.1)
    args = parser.parse_args()

    best = None

    for i in range(args.best_of):
        t0 = time.monotonic()
        subprocess.check_call((sys.executable, '-c', 'import pyparsing'))
        t1 = time.monotonic()

        duration = t1 - t0
        if best is None or duration < best:
            best = duration

    print(f'best of {args.best_of}: {best:.3f}')
    return best >= args.cutoff


if __name__ == '__main__':
    raise SystemExit(main())
