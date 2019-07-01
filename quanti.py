
import numpy as np
import cv2

# Função: imread ( nome da imagem, [1=cor, 0=grayscape, -1=alpha])
# Cada coluna da imagem é armazenada em um subvetor, onde cada coluna é uma posição
img = cv2.imread('wom.jpeg', 0)



## Quantização ##
# 255 / 31 = 8,22...
# Assim, teremos uma imagem com 8 tons de cinza. A conta é feita desta forma para descartar a parte decimal dos números e alterar o vetor para que possua apenas 8 valores possíveis.
r = 31
img = np.uint8(img / r) * r

# Salvar imagem no disco #
#cv2.imwrite('C:/Diretório', img_aum)

# Mostra uma imagem
# Função: cv.imshow(nome da janela, matriz)
cv2.imshow('Quantizada',img)


# Funções para o funcionamento correto do python no Windows.
cv2.waitKey(0)
cv2.destroyAllWindows()