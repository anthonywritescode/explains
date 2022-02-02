import os.path


def mkdirp(s: str) -> None:
    try:
        os.makedirs(s)
    except OSError:
        if not os.path.isdir(s):
            raise
