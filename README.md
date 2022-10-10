# installDonkeycarJetsonNanoJP46-v2
instruction for installation of  donkeycar.com on a Jetson Nano JP 4.6 - version 2 - Oct. 8th 2022

- using [Ed's install script](https://github.com/autorope/donkeycar/tree/990-jetson-nano-install-script)
- see the [logs](logs) for details of the input, output, errors of the trials 

## JP 4.6 Software versions
- virtualenv 20.14.1?
- python 3.6.9
- OpenCV 4.1.1

## Desired Software versions
- python 3.7 
- tensorflow >=2.2.0 (see TCIII list](https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform-release-notes/tf-jetson-rel.html)

## Checks
- [x] installation incl. Ed's script without errors
- [ ] CSI camera
- [ ] usb camera
- [ ] donkey drive & train
- [ ] run prepared [models trained w/ tf 2.2 will work by using any of the models in ](https://github.com/autorope/donkey_datasets/tree/master/circuit_launch_20210716/models)
