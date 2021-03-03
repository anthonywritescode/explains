# [images in the terminal? what is a sixel (beginner - intermediate)](https://youtu.be/fa9ik_OnLmg)

Today I talk about terminal images and one of the implementations (sixels)!

## Interactive examples

### Bash

```bash
xterm -ti 340
dpkg -l | grep sixel
img2sixel --help
img2sixel <image_file>
img2sixel --colors=16 <image_file>
yes | head -2 | xargs --replace img2sixel --colors=16 <image_file>
echo -en '\033[s' img2sixel --colors=16 <image_file> && echo -en '\033[u\033[A1\033[C3' && img2sixel --colors=16 <image_file>
echo -en '\033[s' img2sixel --colors=16 <image_file> && echo -en '\033[u\033[1A\033[3C' && img2sixel --colors=16 <image_file>
img2sixel <image_file> --high-color
echo -en 'hi \033[s' && img2sixel --bgcolor '#2d0922' --height 24 --width 24 --high-color <image_file> && echo -e '\033[u\033[3C\033[1Ahi hello hello' && echo hi hi hi
img2sixel <image_file> > t.sixel
babi !$
```
