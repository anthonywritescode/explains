import argparse
import importlib.metadata
import sys


def default_output(output: str) -> None:
    print(output)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--outputer', default='default')
    args = parser.parse_args()

    eps = importlib.metadata.entry_points()['hello_world.output']
    outputers = {
        entrypoint.name: entrypoint
        for entrypoint in eps
    }

    try:
        outputer = outputers[args.outputer].load()
    except KeyError:
        print(f'outputer {args.outputer} is not available!', file=sys.stderr)
        outputers_s = ', '.join(sorted(outputers))
        print(f'available outputers: {outputers_s}', file=sys.stderr)
        return 1

    outputer('hello world')

    return 0


if __name__ == '__main__':
    exit(main())
