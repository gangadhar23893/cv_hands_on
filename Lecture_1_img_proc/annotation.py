import cv2
import numpy as np

img = cv2.imread(r'/Users/gangadhar/Documents/my_folder/my_projects/Cv_hands_on/comb_2.jpg')
#canvas = np.zeros((400,400,3), dtype="uint8")
print(img.shape)
line = cv2.line(img.copy(),(0,0),(400,400),(0,255,0),5)
#cv2.imshow("Original Image", img)
rectangle = cv2.rectangle(img.copy(),(10,50),(200,200),(255,0,0),5)
text = cv2.putText(rectangle, "OpenCV", (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2)
cv2.imshow("Image", img)
cv2.imshow("Line", line)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("Text", text)    
cv2.waitKey(0)
cv2.destroyAllWindows()