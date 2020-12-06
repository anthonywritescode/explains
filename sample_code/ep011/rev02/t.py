

def main():
    for i in range(10):
        if i == 5:
            print('I found five!')
            break
        print(i)
    else:
        print('else ran!')


if __name__ == '__main__':
    exit(main())
