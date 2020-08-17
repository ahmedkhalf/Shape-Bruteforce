import functools

import numpy as np

# Shape constants are tuples:
# [0] is the shape id
# [1] is the number/len of parameters for that shape
CIRCLE = 0, 7


def random_shape(shape):
    return np.random.rand(shape[1])


def shape(func):
    @functools.wraps(func)
    def wrapper_shape(img, params):
        img.ctx.set_source_rgba(*params[0:4])
        func(img, params)
        img.ctx.fill()
    return wrapper_shape


@shape
def draw_circle(img, params):
    img.ctx.arc(
        xc=params[4] * img.width,
        xy=params[5] * img.height,
        radius=(img.width + img.height) / 4 * params[6],
        angle1=0,
        angle2=np.pi * 2,
    )
