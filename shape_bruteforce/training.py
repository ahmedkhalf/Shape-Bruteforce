import random
import math

import cairo
import numpy as np
import tqdm


class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        self.ctx = cairo.Context(self.surface)

    def draw_background(self, r, g, b, a=1.0):
        self.ctx.set_source_rgba(r, g, b, a)
        self.ctx.rectangle(0, 0, self.width, self.height)
        self.ctx.fill()

    def copy_image(self, img):
        self.ctx.set_source_surface(img.surface)
        self.ctx.paint()

    def to_array(self):
        buf = self.surface.get_data()
        array = np.ndarray(shape=(self.height, self.width, 4), dtype=np.uint8, buffer=buf)
        return array


class Training:
    def __init__(self, target):
        self.th, self.tw = target.shape[0:2]  # target height, target width
        self.target = target
        self.parent = Image(self.tw, self.th)
        self.parent.draw_background(0, 0, 0)

    def mse(self, img):
        arr = img.to_array()
        return float(np.square(np.subtract(arr, self.target)).mean())

    def add_random_circle(self, img):
        child = Image(self.tw, self.th)
        child.copy_image(img)
        child.ctx.set_source_rgba(random.random(), random.random(), random.random(), random.random())
        child.ctx.arc(
            random.uniform(0, self.tw), random.uniform(0, self.th),  # x, y
            random.uniform(0, (self.tw + self.th) / 2 / 2),          # radius
            0, 2 * math.pi)
        child.ctx.fill()
        return child

    def train(self, shape_count=256, gens_per_shape=2000):
        pbar = tqdm.trange(shape_count)
        for i in pbar:
            best_child = self.add_random_circle(self.parent)
            best_child_fit = self.mse(best_child)

            for j in range(gens_per_shape):
                child = self.add_random_circle(self.parent)
                child_fit = self.mse(child)

                if child_fit < best_child_fit:
                    best_child = child
                    best_child_fit = child_fit
                    pbar.set_description("ERR " + str(int(best_child_fit)))

            self.parent = best_child


if __name__ == "__main__":
    from shape_bruteforce import utils
    target = utils.load_image("mona-lisa.jpg")
    target = utils.resize_image(target, 64)
    target = utils.normalize_image(target)
    trainer = Training(target)
    trainer.train()
    arr = trainer.parent.to_array()
    utils.show_image(arr)
