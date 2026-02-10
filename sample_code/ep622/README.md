# [making the "slurp" video](https://youtu.be/UhRzwSCiZm4)

today I walk through how I made this: [• 2025_slurp.mov](https://www.youtube.com/watch?v=4tsmLkPX1hU)

## Setup commands

```bash
git clone git@github.com:anthonywritescode/slurp
git clone git@github.com:asottile/nintendo-microcontrollers
```

## Interactive examples

### Bash

```bash
cd slurp/
xdg-open 6.png

cd ../nintendo-microcontrollers/
python3 debug_screen_hsv.py ../slurp/300.png

python t.py 300.png
xdg-open <crop>.png
```
