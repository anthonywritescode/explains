from typing import NamedTuple


class User(NamedTuple):
    name: str
    age: int
    location: str = 'unknown'

    def print_me(self):
        print(f'{self.name} is {self.age} years old and from {self.location}')


def get_users():
    return [
        User('Anthony', 29, 'CA'),
        User('Jeff', 18, 'NY'),
        User('Jason', 16, 'GB'),
        User('Carmen San Diego', 32),
    ]
