def main() -> int:
    while True:
        print('what would you like to do?')
        print('1: greet with hi')
        print('2: greet with hello')
        print('q: quit')

        response = input('> ')
        if response == '1':
            print('hi hi')
        elif response == '2':
            print('hello hello')
        elif response == 'q':
            print('bye bye')
            return 0
        else:
            print(f'unexpected response: {response}')


if __name__ == '__main__':
    exit(main())
