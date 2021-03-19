import io
import tokenize


def main():
    with open('Lib/test/test_socket.py', 'rb') as f:
        contents = io.BytesIO(f.read())

    for _ in range(5):
        contents.seek(0)
        for _ in tokenize.tokenize(contents.readline):
            pass


if __name__ == '__main__':
    exit(main())
