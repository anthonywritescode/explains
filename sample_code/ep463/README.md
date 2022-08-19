# [relocatable macos binaries (advanced)](https://youtu.be/OL7JTiJs-d8)

I made a previous video about using `rpath` to make relocatable linux binaries -- unfortunately there's a bit more work to make it work on macos as well.  I go over how to look at dynamically linked things and how to achieve relocatable binaries!

## Interactive examples

### Bash

```bash
babi t.c
curl -o t.c https://raw.githubusercontent.com/anthonywritescode/explains/main/sample_code/ep413/rev01/t.c

uname -a
brew install libsass

gcc -lsass t.c -o main
gcc -I$(brew --prefix libsass)/include -L$(brew --prefix libsass)/lib -lsass t.c -o main
./main

otool -L ./main
ls /usr/lib/libSystem.B.dylib
otool -l ./main

brew uninstall libsass
./main

brew install libsass
./main

mkdir lib
cp $(brew --prefix libsass)/lib/libsass.1.dylib lib/
ls /usr/lib/libc++.1.dylib

install_name_tool -id @loader_path/libsass.1.dylib lib/libsass.1.dylib
codesign --force --sign - lib/libsass.1.dylib

otool -L main
ls lib/
install_name_tool -change $(brew --prefix libsass)/lib/libsass.1.dylib @loader_path/lib/libsass.1.dylib ./main
otool -L main
otool -L lib/libsass.1.dylib

./main
brew uninstall libsass
./main

ls lib/
ls
```
