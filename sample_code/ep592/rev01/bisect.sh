#!/usr/bin/env bash
set -euxo pipefail

git clean -fxfd
cd src && bash make.bash

cd ..
export "PATH=$PWD/bin:$PATH"

cd ~/cgo-repro
make clean
make
