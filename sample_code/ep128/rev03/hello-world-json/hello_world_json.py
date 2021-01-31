import json


def json_output(output: str) -> None:
    print(json.dumps({'output': output}))
