# [what is a universal2 wheel? (intermediate)](https://youtu.be/utdohIoR9ZM)

Today I talk about what a `universal2` wheel is for macos and why it's a "2"!

## Interactive examples

### Bash

Session 1:

```bash
wget https://files.pythonhosted.org/packages/99/5f/87c3fafadd590ee42ad5253c5e09061a7efa1495adc2415d1ae137fca326/simplejson-3.17.3-cp38-cp38-macosx_10_9_universal2.whl#sha256=2104475a0263ff2a3dffca214c9676eb261e90d06d604ac7063347bd289ac84c

unzip simplejson-3.17.3-cp38-cp38-macosx_10_9_universal2.whl

find -name '*.so'
file ./simplejson/_speedups.cpython-38-darwin.so
ls -al !$
du -hs !$
```

Session 2:

```bash
mkdir y
cd !$

wget https://files.pythonhosted.org/packages/da/fd/1ae4ea6d4a06239b0a0829ddb78633c3774e170a2fcbf659a2a3d09181a8/simplejson-3.17.3-cp38-cp38-macosx_10_9_x86_64.whl#sha256=fed5e862d9b501c5673c163c8593ebdb2c5422386089c529dfac28d70cd55858
unzip simplejson-3.17.3-cp38-cp38-macosx_10_9_x86_64.whl
du -hs ./simplejson/_speedups.cpython-38-darwin.so
```
