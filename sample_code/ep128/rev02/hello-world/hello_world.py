import argparse
import importlib.metadata


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
    outputer = outputers[args.outputer].load()

    outputer('hello world')

    return 0


if __name__ == '__main__':
    exit(main())
