from a import g


class B:
    def say_hello(self) -> None:
        g()


def main() -> int:
    b = B()
    b.say_hello()
    return 0


if __name__ == '__main__':
    exit(main())
