from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import Protocol
else:
    Protocol = object


class MyProtocol(Protocol):
    def __getitem__(self, x: int) -> int: ...


class C:
    def __getitem__(self, x: int) -> int:
        return x * x


def f(indexable: MyProtocol) -> None:
    print(f'hello hello {indexable[9]}')


def main() -> int:
    f(C())
    return 0


if __name__ == '__main__':
    exit(main())
