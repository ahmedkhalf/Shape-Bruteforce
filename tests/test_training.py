import shape_bruteforce as sb
import unittest
import numpy as np


class TestImage(unittest.TestCase):
    def test_init_image(self):
        sb.training.Image(400, 400)

    def test_image_array(self):
        image = sb.training.Image(400, 600)
        arr = image.to_array()
        self.assertTrue(arr.shape == (600, 400, 4))

    def test_copy_image(self):
        image1 = sb.training.Image(400, 400)
        image1.ctx.set_source_rgb(0, 0, 0)
        image1.ctx.rectangle(0, 0, 100, 100)
        image1.ctx.fill()
        image2 = sb.training.Image(400, 400)
        image2.copy_image(image1)
        arr1 = image1.to_array()
        arr2 = image2.to_array()
        self.assertTrue(np.array_equal(arr1, arr2))


if __name__ == '__main__':
    unittest.main()
