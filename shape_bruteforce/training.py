import cairo
import numpy as np


class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        self.ctx = cairo.Context(self.surface)

    def copy_image(self, img):
        self.ctx.set_source_surface(img.surface)
        self.ctx.paint()

    def to_array(self):
        buf = self.surface.get_data()
        array = np.ndarray(shape=(self.height, self.width, 4), dtype=np.uint8, buffer=buf)
        return array


def train():
    pass
