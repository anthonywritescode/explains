# [easily try rust as a python dev (intermediate)](https://www.youtube.com/watch?v=ZGlEIetFNf0)

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
