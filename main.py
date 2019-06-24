import cv2
import numpy

import reshape

image = cv2.imread("wom16.jpg", 0)

imagem_blocos = reshape.divide_image(image, 8, 8)
imagem_reconstruida = reshape.rebuild_image(imagem_blocos, image.shape[0], image.shape[1])

imf = numpy.float32(imagem_blocos[0])/255.0  # float conversion/scale
dct = cv2.dct(imf)                  # the dct
idct = cv2.idct(dct)
img_dct = numpy.uint8((idct * 255.0))    # convert back

# print imagem
print("image original")
print(image)
print("image blocos")
print(imagem_blocos)

print("dct")
print(dct)
print(idct)
print(img_dct)
print(imagem_blocos[0])
print()

print("image reconstruida")
print(imagem_reconstruida)