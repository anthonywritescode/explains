import os.path
import json
import random
import shutil


shutil.rmtree('split', ignore_errors=True)
os.makedirs('split/train')
os.makedirs('split/val')
os.makedirs('split/test')

r = random.Random(0)

fnames = [os.path.splitext(fname)[0] for fname in os.listdir('exports/images')]
r.shuffle(fnames)

imgnames = [f'export/images/{fname}.png' for fname in fnames]
labnames = [f'export/labels/{fname}.txt' for fname in fnames]

stop1 = int(len(fnames) * .7)
stop2 = int(len(fnames) * .9)


def cp(names, dest):
    for name in names:
        shutil.copy(name, dest)


cp(imgnames[:stop1], 'split/train')
cp(labnames[:stop1], 'split/train')

cp(imgnames[stop1:stop2], 'split/val')
cp(labnames[stop1:stop2], 'split/val')

cp(imgnames[stop2:], 'split/test')
cp(labnames[stop2:], 'split/test')

conf = {
    'nc': 3,
    'names': ['p', 'p2', 'pz'],
    'train': os.path.abspath('split/train'),
    'val': os.path.abspath('split/val'),
    'test': os.path.abspath('split/test'),
}

with open('split/data.yaml', 'w') as f:
    json.dump(conf, f)
