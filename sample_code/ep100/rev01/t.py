

# def get_users() - List[Tuple[str, int, str]]:
def get_users():
    return [
        ('Anthony', 29, 'CA'),
        ('Jeff', 18, 'NY'),
        ('Jason', 16, 'GB'),
    ]


for name, age, location in get_users():
    print(f'{name} is {age} years old and from {location}')
