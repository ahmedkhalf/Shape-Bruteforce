import shape_bruteforce as sb
import unittest
import pathlib


class TestLoad(unittest.TestCase):
    def setUp(self):
        self.path = pathlib.Path(__file__).parent.joinpath("fixtures", "mona-lisa.jpg")
        self.path = str(self.path)

    def test_load(self):
        sb.utils.load_image(self.path)

    def test_no_load(self):
        with self.assertRaises(FileNotFoundError):
            sb.utils.load_image("ifejfijfjej6969.frok")


class TestResize(unittest.TestCase):
    def setUp(self):
        self.path = pathlib.Path(__file__).parent.joinpath("fixtures", "mona-lisa.jpg")
        self.path = str(self.path)
        self.img = sb.utils.load_image(self.path)

    def test_resize_height(self):
        image = sb.utils.resize_image(self.img, 64, mode=sb.utils.RESIZE_HEIGHT)
        self.assertEqual(image.shape[0], 64)

    def test_resize_width(self):
        image = sb.utils.resize_image(self.img, 64, mode=sb.utils.RESIZE_WIDTH)
        self.assertEqual(image.shape[1], 64)

    def test_resize_min(self):
        image = sb.utils.resize_image(self.img, 64, mode=sb.utils.RESIZE_MIN)
        self.assertEqual(image.shape[1], 64)

    def test_resize_max(self):
        image = sb.utils.resize_image(self.img, 64, mode=sb.utils.RESIZE_MAX)
        self.assertEqual(image.shape[0], 64)


if __name__ == '__main__':
    unittest.main()
