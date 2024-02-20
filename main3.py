import cv2
import os

img=cv2.imread("C:/Users/Anukriti/Desktop/all my files (anukriti)/open cv/l-1/pika.png",0)

cv2.imshow("pokem",img)

path="C:/Users/Anukriti/Desktop/all my files (anukriti)/open cv/l-1"

os.chdir(path)

cv2.imwrite("bnw.png",img)

print("saved")

cv2.waitKey(0)
cv2.destroyAllWindows()