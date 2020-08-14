import cv2
from matplotlib import pyplot
import numpy as np
import os
from shape_bruteforce import _version

RESIZE_MAX = 0
RESIZE_MIN = 1
RESIZE_HEIGHT = 2
RESIZE_WIDTH = 3


def get_version():
    """Version info"""
    return _version.__version__


def load_image(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Image was not found at {path}")

    img = cv2.imread(path)
    return img


def normalize_image(img):
    shape = img.shape
    if img.ndim == 3:
        if shape[2] == 4:
            return img
        elif shape[2] == 3:
            img = np.dstack((img, np.ones((shape[0], shape[1])) * 255))
            return img
    elif img.ndim == 2:
        pass
    raise NotImplementedError()


def _resize_height(img, max_size):
    height, width = img.shape[0:2]
    if height < max_size:
        return img
    scale_factor = max_size / height
    width = int(width * scale_factor)
    img = cv2.resize(img, (width, max_size), interpolation=cv2.INTER_AREA)
    return img


def _resize_width(img, max_size):
    height, width = img.shape[0:2]
    if width < max_size:
        return img
    scale_factor = max_size / width
    height = int(height * scale_factor)
    img = cv2.resize(img, (max_size, height), interpolation=cv2.INTER_AREA)
    return img


def resize_image(img, max_size, mode=RESIZE_MIN):
    height, width = img.shape[0:2]
    if mode == RESIZE_MIN:
        if height < width:
            img = _resize_height(img, max_size)
        else:
            img = _resize_width(img, max_size)
    elif mode == RESIZE_MAX:
        if height > width:
            img = _resize_height(img, max_size)
        else:
            img = _resize_width(img, max_size)
    elif mode == RESIZE_HEIGHT:
        img = _resize_height(img, max_size)
    else:  # RESIZE_WIDTH
        img = _resize_width(img, max_size)

    return img


def show_image(img):
    pyplot.imshow(img)
    pyplot.show()
