# Logs
This directory contains the documentation of the sevaral installation trials NN:
- input__NN.log
- output_NN.log
- errors_NN.log

# Installation trials

## 1 base installation, Oct. 9th 2022
- error: tensorflow & donkey
```
SyntaxError: future feature annotations is not defined
```
- possible fix: use python 3.7.x
- link: https://stackoverflow.com/questions/52889746/cant-import-annotations-from-future

## 2 python 3.7.14 using pyenv, Oct. 9th 2022
- error: 
```
CSI & WEBCAM cameras do not work
```
- possible fix: check which version of tensorflow, OpenCV, JP works together
- link: https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform-release-notes/tf-jetson-rel.html
