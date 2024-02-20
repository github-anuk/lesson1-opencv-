import cv2

img=cv2.imread("C:/Users/Anukriti/Desktop/all my files (anukriti)/open cv/l-1/pika.png",1)


# There are 3 parameters to read an image - 
#cv2.IMREAD_COLOR (1) => Specify to load the image in color. excludes transaperency
#cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
#cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged

cv2.imshow("pika",img)

cv2.waitKey(0)
cv2.destroyAllWindows()