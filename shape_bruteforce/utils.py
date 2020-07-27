import cv2
from matplotlib import pyplot
import os
from shape_bruteforce import _version


def get_version():
    """Version info"""
    return _version.__version__


def load_image(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Image was not found at {path}")

    img = cv2.imread(path)
    return img


def show_image(img):
    pyplot.imshow(img)
    pyplot.show()
