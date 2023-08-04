import sys
import tokenize


def main() -> int:
    for fname in sys.argv[1:]:
        with open(fname) as f:
            for _ in tokenize.generate_tokens(f.readline):
                pass
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
