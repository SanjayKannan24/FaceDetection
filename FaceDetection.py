import tensorflow as tf
import cv2
import json
import numpy as np
from matplotlib import pyplot as plt

# Setting GPU memory consumption growth in order to avoid OOM errors
gpu = tf.config.experimental.list_physical_devices('GPU')
for i in gpu:
    tf.config.experimental.set_memory_growth(i , True)

# Check is the GPU available or not
tf.config.list_physical_devices('GPU')
print("done")