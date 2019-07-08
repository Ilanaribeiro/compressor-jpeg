import cv2
import numpy as np



img1 = cv2.imread("dog.jpeg",0)
imgSize = img1.shape
ImgQuantizada = np.zeros(imgSize)
i= np.array(img1)

             
Quant=np.array([[16,11,10,16,24,40,51,61],
                         [12,12,14,19,26,48,60,55],
                         [14,13,16,24,40,57,69,56],
                         [14,17,22,29,51,87,80,62],
                         [18,22,37,56,68,109,103,77],
                         [24,35,55,64,81,104,113,92],
                         [49,64,78,87,103,121,120,101],
                         [72,92,95,98,112,100,103,99]])

for x in range(0, imgSize[0], 8): 
        for y in range(0, imgSize[1], 8): 
                ImgQuantizada[x:(x + 8), y:(y + 8)] = i[x:(x + 8), y:(y + 8)]//Quant


print(ImgQuantizada)

cv2.imshow('', ImgQuantizada) 
cv2.waitKey()