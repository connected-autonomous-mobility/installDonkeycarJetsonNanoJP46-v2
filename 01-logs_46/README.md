# 01-Logs46
This directory contains the documentation of the sevaral installation trials NN:
- NN-input.log
- NN-output.log
- NN-errors.log

# Installation trials
-using: [Ed's install script](https://github.com/autorope/donkeycar/tree/990-jetson-nano-install-script)

## 01 base installation, Oct. 9th 2022
- error: tensorflow & donkey
```
SyntaxError: future feature annotations is not defined
```
- possible fix: use python 3.7.x
- link: https://stackoverflow.com/questions/52889746/cant-import-annotations-from-future

## 02 python 3.7.14 using pyenv, Oct. 9th 2022
- error: 
```
CSI & WEBCAM cameras do not work
```
- possible fix: check which version of tensorflow, OpenCV, JP works together
- link: https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform-release-notes/tf-jetson-rel.html

## 03 tbd
- pip install opencv-python== 
- [get possible OpenCV versions](https://stackoverflow.com/questions/44439443/python-how-to-pip-install-opencv2-with-specific-version-2-4-9#44439955)
- Easy and simple

Prerequisites
pip install matplotlib
pip install numpy
Final step
pip install opencv-python
Specific version * Final step * opencv-python==2.4.9

