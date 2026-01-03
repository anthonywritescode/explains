#!/usr/bin/env bash
set -x
./configure >& /dev/null || exit 125
make -j5 >& /dev/null || exit 125
export PATH=$PWD:$PATH
cd ../repro
bash repro2.sh
