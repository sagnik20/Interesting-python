import cv2
import sys

image = cv2.imread("sagnik.jpg")
greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
greyImageInv = 255 - greyImage
greyImageInv = cv2.GaussianBlur(greyImageInv,(21,21),0)
output = cv2.divide(greyImage,255-greyImageInv, scale = 256.0)
cv2.namedWindow("image",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("pencilSketch",cv2.WINDOW_AUTOSIZE)
cv2.imshow("image", image)
cv2.imshow("pencilSketch", output)
cv2.waitKey(0)
cv2.destroyAllWindows()