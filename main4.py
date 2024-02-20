import cv2

img=cv2.imread("C:/Users/Anukriti/Desktop/all my files (anukriti)/open cv/l-1/pika.png",1)
 
B, G, R = cv2.split(img)

cv2.imshow("oringnal",img)
cv2.waitKey(delay= 5000)
cv2.destroyWindow("oringnal")

cv2.imshow("bsi",B)
cv2.waitKey(delay= 5000)
cv2.destroyWindow("bsi")

cv2.imshow("rsi",R)
cv2.waitKey(delay= 5000)
cv2.destroyWindow("rsi")

cv2.imshow("gsi",G)
cv2.waitKey(delay= 5000)
cv2.destroyWindow("gsi")

