# [how I use selenium + html/css to make thumbnails (intermediate)](https://youtu.be/VABA2rX1I_M)

Why are all your thumbnails so uniform? I show my mostly-automated process for generating thumbnails for videos!

## Setup commands

```bash
git clone https://github.com/anthonywritescode/thumbnails
# git clone git@github.com:anthonywritescode/thumbnails

cd thumbnails

make

. venv/bin/activate

pip install future-breakpoint
```

## Interactive examples

### Python debugger (pdb)

```
p 'p means print'
p 'n means next'
p 'q means quit'
n
driver.find_element_by_css_selector('span')
driver.find_element_by_css_selector('span').text
driver.find_element_by_css_selector('span').click()
list
n
n
n
n
n
q
```

### Bash

```bash
./make-screenshot.py explains.htm

nautilus .
```
