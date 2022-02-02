import os.path


def mkdirp(s: str) -> None:
    try:
        os.makedirs(s)
    except OSError as e:
        if not os.path.isdir(s):
            raise e
