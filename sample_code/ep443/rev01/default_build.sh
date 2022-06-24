# git clone https://github.com/python/cpython
git clone git@github.com:python/cpython --depth=1 -b v2.7.18
cd cpython

./configure --prefix="$PWD/prefix"
make -j5
make install
