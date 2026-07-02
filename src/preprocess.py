"""
Frame preprocessing for ConvNeXt V2 ONNX inference.
"""

import cv2
import numpy as np


IMAGE_SIZE = 224


def preprocess(frame):
    """
    Convert an OpenCV frame into an ONNX model input.
    """

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    image = cv2.resize(image, (IMAGE_SIZE, IMAGE_SIZE))

    image = image.astype(np.float32) / 255.0

    image = np.transpose(image, (2, 0, 1))

    image = np.expand_dims(image, axis=0)

    return image