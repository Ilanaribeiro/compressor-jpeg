import numpy as np
import scipy.interpolate as interpolate


def downsample(image, factor):
    """
    Downsample a 8x8 image by the downsampling factor defined as (4, 4, 4)
    """
    if factor == (4, 4, 4):
        return image
    elif factor == (4, 2, 2):
        return image[::2, ::]
    elif factor == (4, 2, 0):
        return image[::2, ::2]


def upsample(image):
    """
    Upsample a image with scipy.interpolate.griddata
    """
    line, column = image.shape
    vals = np.reshape(image, (line * column))
    pts = np.array([[i, j] for i in np.linspace(0, 1, line) for j in np.linspace(0, 1, column)])
    original_image_shape = 8j
    grid_x, grid_y = np.mgrid[0:1:original_image_shape, 0:1:original_image_shape]
    return interpolate.griddata(pts, vals, (grid_x, grid_y), method='linear')