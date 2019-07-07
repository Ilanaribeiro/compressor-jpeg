import cv2

import colorspaces
import sampling
import reshape
import dct

image = cv2.imread("dog.jpeg")

y, cr, cb = colorspaces.rgb2ycrcb(image)

original_image_shape = y.shape
downsample_factor = (4, 4, 4)

print("Initializing downsampling")
downsampled_cr = sampling.downsample(cr, downsample_factor)
downsampled_cb = sampling.downsample(cb, downsample_factor)

y_blocks = reshape.divide_image(y, 8, 8)
cr_blocks = reshape.divide_image(downsampled_cr, 8, 8)
cb_blocks = reshape.divide_image(downsampled_cb, 8, 8)
# TODO Adicionar tratamento para divisão de imagens não múltiplas de 8.
# TODO Levar em consideração o downsample com todos os fatores

# This step reduces the dynamic range requirements in the DCT processing stage that follows.
# y_shifted_blocks = y_blocks - 128
# cr_shifted_blocks = cr_blocks - 128
# cb_shifted_blocks = cb_blocks - 128


y_dct_blocks, cr_dct_blocks, cb_dct_blocks = dct.dct_from_ycrcb_blocks(y_blocks, cr_blocks, cb_blocks)


# TODO Quantização da imagem entra aqui. @João
# https://en.wikipedia.org/wiki/Quantization_(image_processing)#Quantization_matrices

y_idct_blocks, cr_idct_blocks, cb_idct_blocks = dct.idct_from_ycrcb_dct_blocks(y_dct_blocks, cr_dct_blocks, cb_dct_blocks)


# y_unshifted_blocks = y_blocks + 128
# cr_unshifted_blocks = cr_blocks + 128
# cb_unshifted_blocks = cb_blocks + 128


y_idct_image = reshape.rebuild_image(y_idct_blocks, original_image_shape)
cr_idct_image = reshape.rebuild_image(cr_idct_blocks, original_image_shape)
cb_idct_image = reshape.rebuild_image(cb_idct_blocks, original_image_shape)


print("Initializing upsampling")
upsampled_cr = sampling.upsample(cr_idct_image, original_image_shape)
print("Done upsampling cr")
upsampled_cb = sampling.upsample(cb_idct_image, original_image_shape)
print("Done upsampling cb")

image2 = colorspaces.ycrcb2rgb(y, upsampled_cr, upsampled_cb)

cv2.imshow('image', image)
cv2.imshow('image2', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
