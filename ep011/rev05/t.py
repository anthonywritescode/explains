

def main():
    for i in range(10):
        if i == 5:
            print('I found five!')
            raise AssertionError('ohnoes!')
        print(i)

    print('else ran!')


if __name__ == '__main__':
    exit(main())
