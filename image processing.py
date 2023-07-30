# create new file with name image_processing
# here * stands for file name

# windows bitmaps = *.bmp, *.dib
# TIFF files = *.tiff,*.tif
# JEPG = *.jp




'''Syntax for reading an image
    cv2.imread('path',flag)'''

import cv2

img = cv2.imread("C:/Users/Arundhati",cv2.IMREAD_COLOR)

cv2.imshow("original image", img)

img2 = cv2.imread("img.png")
cv2.imshow("Second Image", img2)


cv2.waitKey(0) # to hold image on the screen waitKey function is used

cv2.destroyAllWindows() # for deleting or removing GUI from memory and screen destroyAllWindows function is used

