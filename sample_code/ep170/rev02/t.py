import subprocess
from typing import Union


def output(*cmd: str, text: bool = False) -> Union[bytes, str]:
    return subprocess.check_output(cmd, text=text)


print(output('echo', 'hi'))
print(output('echo', 'hi', text=True))

reveal_type(output('echo', 'hi'))
reveal_type(output('echo', 'hi', text=True))
