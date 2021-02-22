import subprocess
from typing import Final
from typing import Literal
from typing import overload
from typing import Union


@overload
def output(*cmd: str, text: Literal[True]) -> str: ...
@overload
def output(*cmd: str, text: Literal[False] = False) -> bytes: ...


def output(*cmd: str, text: bool = False) -> Union[bytes, str]:
    return subprocess.check_output(cmd, text=text)


# Union[Literal['passed'], Literal['failed'], Literal['errored']]
# Literal['passed', 'failed', 'errored']

PASSED: Literal['passed'] = 'passed'
FAILED: Final = 'failed'


def report_status(status: Literal['passed', 'failed', 'errored']): ...


print(output('echo', 'hi'))
print(output('echo', 'hi', text=True))

reveal_type(output('echo', 'hi'))
reveal_type(output('echo', 'hi', text=True))
