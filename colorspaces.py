import cv2


def rgb2ycrcb(rgb_image):
    imgYCC = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2YCR_CB)
    y, cr, cb = cv2.split(imgYCC)
    return y, cr, cb
    

def ycrcv2rgb(y, cr, cb):
    imgYCC = cv2.merge([y, cr, cb])
    return cv2.cvtColor(imgYCC, cv2.COLOR_YCR_CB2BGR)