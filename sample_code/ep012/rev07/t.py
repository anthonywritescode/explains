

for i in range(50):
    if i == 15:
        pass
    elif i % 3 == 0 and i % 5 == 0:
        print(f'{i} fizzbuzz')
    elif i % 3 == 0:
        print(f'{i} fizz')
    elif i % 5 == 0:
        print(f'{i} buzz')
        breakpoint()
        pass
