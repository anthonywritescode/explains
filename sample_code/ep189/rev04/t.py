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
    # option 3
    with contextlib.ExitStack() as ctx:
        streams = [stream]
        if filename is not None:
            streams.append(ctx.enter_context(open(filename, 'w')))

        for output_stream in streams:
            output_stream.write(f'{s}\n')


output_line('hello world', stream=sys.stdout)
output_line('goodbye world', stream=sys.stdout, filename='log.log')
