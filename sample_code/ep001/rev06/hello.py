import argparse


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('person')
    args = parser.parse_args(argv)

    print(f'Hello Sexy Person {args.person}')


if __name__ == '__main__':
    main()
