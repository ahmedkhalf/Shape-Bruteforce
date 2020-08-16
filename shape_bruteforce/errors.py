class ImageDepthError(Exception):
    """Exception raised when depth (third axis) is not what it should be
    """

    def __init__(self, given_depth, expected_depths):
        self.message = f"Unexpected image depth: {given_depth}, expected {expected_depths}."
        super().__init__(self.message)


class ImageDimensionError(Exception):
    """Exception raised number of dimensions is not what it should be
    """

    def __init__(self, given_dim, expected_dims):
        self.message = f"Unexpected image dimension: {given_dim}, expected {expected_dims}."
        super().__init__(self.message)
