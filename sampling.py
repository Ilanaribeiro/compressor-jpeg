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


def upsample(image, original_image_shape):
    """
    Upsample a image with scipy.interpolate.griddata
    """
    nlines, ncolumns = image.shape
    original_nlines, original_ncolumns = original_image_shape
    vals = np.reshape(image, (nlines * ncolumns))
    pts = np.array([[i, j] for i in np.linspace(0, 1, nlines) for j in np.linspace(0, 1, ncolumns)])
    grid_x, grid_y = np.mgrid[0:1:complex(0, original_nlines), 0:1:complex(0, original_ncolumns)]
    return interpolate.griddata(pts, vals, (grid_x, grid_y), method='linear').astype("uint8")