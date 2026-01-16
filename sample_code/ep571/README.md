#  [training a custom object detection model from scratch (yolov8) (intermediate)](https://youtu.be/ZG38vpkSHlM)

today I walk through my adventures training a custom object detection model (for identifying pokemon)!

## Setup commands

```bash
docker pull heartexlabs/label-studio:latest
docker run --rm -it -p 8080:8080 -v $(pwd)/mydata:/label-studio/data heartexlabs/label-studio:latest
mkdir mydata
docker run --user 0 --rm -it -p 8080:8080 -v $(pwd)/mydata:/label-studio/data heartexlabs/label-studio:latest

```

## Interactive examples

### Bash

```bash
xdg-open images/<image_name>.png

ls ~/Downloads/
mkdir y
cd !$
unzip ~/Downloads/project-1*.zip
```

### Windows CMD

```batch
chdir /d E:
cd modeling

babi split_dataset.py
venv\Scripts\python.exe split_dataset.py

venv-oops-cpu\Scripts\activate
yolo check

venv-with-gpu\Scripts\activate
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
yolo check

babi split/data.yaml
ls -al split

train.bat
test.bat
```
