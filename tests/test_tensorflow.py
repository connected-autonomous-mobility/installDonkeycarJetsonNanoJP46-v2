# https://stackoverflow.com/questions/55691174/check-whether-tensorflow-is-running-on-gpu

import tensorflow as tf
if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
    print(f"tensorflow version: {tf.__version__}")
else:
    print("Please install GPU version of TF")
