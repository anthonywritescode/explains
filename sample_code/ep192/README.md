# [useful tools: uq (beginner - intermediate)](https://youtu.be/K8jmAQnPE2c)

Today I show off a cool little tool: `uq` -- the "universal serializer".  it's useful for chaining configuration file contents to the jq (a json querying tool)

## Interactive examples

### Bash

```bash
go get github.com/solarkennedy/uq
ls ~/go/bin/
export PATH=~/go/bin:$PATH
which uq
uq <input_file> | jq .repos[].repo
uq <input_file> | jq --raw-output .repos[].repo
uq --format toml <input_file>
```
