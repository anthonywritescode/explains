import sys
from typing import IO
from typing import Optional


def output_line(
        s: str,
        stream: IO[str],
        *,
        filename: Optional[str] = None,
) -> None:
    # option 1
    if filename is not None:
        with open(filename, 'w') as f:
            for output_stream in (f, stream):
                output_stream.write(f'{s}\n')
    else:
        stream.write(f'{s}\n')


output_line('hello world', stream=sys.stdout)
output_line('hello world', stream=sys.stdout, filename='log.log')
