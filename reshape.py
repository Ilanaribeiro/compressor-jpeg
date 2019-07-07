import numpy as np

def divide_image(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array looks like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    blocks = (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1, 2)
               .reshape(-1, nrows, ncols))

    return np.float32(blocks)


def rebuild_image(arr, original_image_shape):
    """
    Return an array of shape (h, w) = original_image_shape where
    h * w = arr.size

    If arr is of shape (n, nrows, ncols), n sublocks of shape (nrows, ncols),
    then the returned array preserves the "physical" layout of the sublocks.
    """
    h, w = original_image_shape
    n, nrows, ncols = arr.shape
    img =  (arr.reshape(h//nrows, -1, nrows, ncols)
               .swapaxes(1, 2)
               .reshape(h, w))

    return np.uint8(img)