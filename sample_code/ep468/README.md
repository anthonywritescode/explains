# [easy try rust as a python dev (intermediate)](https://youtu.be/ZGlEIetFNf0)

I've been doing some rust recently and I wanted to show off a simple tool that makes it easy to make "rust virtualenvs"

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate

pip install rustenv
rustenv renv
. renv/bin/activate

which rustc
which cargo

cargo init hello-world
tree hello-world/
cd hello-world/
ls
nano Cargo.toml
nano src/main.rs
cargo run
```
