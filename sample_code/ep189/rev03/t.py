import contextlib
import sys
from typing import IO
from typing import Optional


@contextlib.contextmanager
def empty():
    yield


def output_line(
        s: str,
        stream: IO[str],
        *,
        filename: Optional[str] = None,
) -> None:
    # option 2
    if filename is not None:
        f = open(filename, 'w')
        streams = [stream, f]
        ctx = f
    else:
        streams = [stream]
        ctx = contextlib.nullcontext()

    with ctx:
        for output_stream in streams:
            output_stream.write(f'{s}\n')


output_line('hello world', stream=sys.stdout)
output_line('goodbye world', stream=sys.stdout, filename='log.log')
