import cv2
import numpy as np

import colorspaces
import sampling
import reshape
import dct
import entropy

Quant=np.array([[16,11,10,16,24,40,51,61],
                [12,12,14,19,26,48,60,55],
                [14,13,16,24,40,57,69,56],
                [14,17,22,29,51,87,80,62],
                [18,22,37,56,68,109,103,77],
                [24,35,55,64,81,104,113,92],
                [49,64,78,87,103,121,120,101],
                [72,92,95,98,112,100,103,99]])


image = cv2.imread("dog.jpeg")

# RGB -> YCRCB
y, cr, cb = colorspaces.rgb2ycrcb(image)

downsample_factor = (4, 2, 0)

print("Initializing downsampling")
downsampled_cr = sampling.downsample(cr, downsample_factor)
downsampled_cb = sampling.downsample(cb, downsample_factor)

original_image_shape = y.shape
downsampled_shape = downsampled_cr.shape

# Divide imagens em blocos de 8x8
y_blocks = reshape.divide_image(y, 8, 8) # [ [8x8], [8x8] ]
cr_blocks = reshape.divide_image(downsampled_cr, 8, 8)
cb_blocks = reshape.divide_image(downsampled_cb, 8, 8)


y_blocks = y_blocks - 128
cr_blocks = cr_blocks - 128
cb_blocks = cb_blocks - 128


y_dct_blocks = dct.dct_from_blocks(y_blocks)
cr_dct_blocks = dct.dct_from_blocks(cr_blocks)
cb_dct_blocks = dct.dct_from_blocks(cb_blocks)


y_dct_blocks  = np.round((y_dct_blocks / Quant), 4)
cr_dct_blocks = np.round((cr_dct_blocks / Quant), 4)
cb_dct_blocks = np.round((cb_dct_blocks / Quant), 4)


y_list_values = [entropy.zigzag_ordering(block) for block in y_dct_blocks]
cr_list_values = [entropy.zigzag_ordering(block) for block in cr_dct_blocks]
cb_list_values = [entropy.zigzag_ordering(block) for block in cb_dct_blocks]


dc_coefficients = [entropy.get_DC_coefficients(ol) for ol in (y_list_values + cr_list_values + cb_list_values)]


y_symbols_list = [entropy.get_symbols(ordered_list) for ordered_list in y_list_values]
cr_symbols_list = [entropy.get_symbols(ordered_list) for ordered_list in cr_list_values]
cb_symbols_list = [entropy.get_symbols(ordered_list) for ordered_list in cb_list_values]


y_dct_blocks  = y_dct_blocks * Quant
cr_dct_blocks = cr_dct_blocks * Quant
cb_dct_blocks = cb_dct_blocks * Quant


y_idct_blocks = dct.idct_from_blocks(y_dct_blocks)
cr_idct_blocks = dct.idct_from_blocks(cr_dct_blocks)
cb_idct_blocks = dct.idct_from_blocks(cb_dct_blocks)


y_idct_blocks = y_idct_blocks + 128
cr_idct_blocks = cr_idct_blocks + 128
cb_idct_blocks = cb_idct_blocks + 128


y_idct_image = reshape.rebuild_image(y_idct_blocks, original_image_shape)
cr_idct_image = reshape.rebuild_image(cr_idct_blocks, downsampled_shape)
cb_idct_image = reshape.rebuild_image(cb_idct_blocks, downsampled_shape)


print("Initializing upsampling")
upsampled_cr = sampling.upsample(cr_idct_image, original_image_shape)
print("Done upsampling cr")
upsampled_cb = sampling.upsample(cb_idct_image, original_image_shape)
print("Done upsampling cb")

image2 = colorspaces.ycrcb2rgb(y_idct_image, upsampled_cr, upsampled_cb)

cv2.imshow('image', image)
cv2.imshow('image after processing', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
