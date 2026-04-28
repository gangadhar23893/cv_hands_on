import cv2

img=cv2.imread(r'/Users/gangadhar/Documents/my_folder/my_projects/Cv_hands_on/comb_2.jpg')

# 1) resizing 2) greyscale 3) blurring 4) edge detection
# 1) resizing
print(img.shape)
resize = cv2.resize(img, (400, 400)) 
print(resize.shape)

#2) greyscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#3) blurring
blur1 = cv2.GaussianBlur(img, (5,5), 0)
blur2 = cv2.GaussianBlur(img, (15,15), 0)
blur3 = cv2.GaussianBlur(img, (25,25), 0)   

#4) edge detection
canny = cv2.Canny(img, 50, 150)

cv2.imshow("image", img)
cv2.imshow("resized image", resize)
cv2.imshow("greyscale image", gray)
cv2.imshow("blurred image1", blur1)
cv2.imshow("blurred image2", blur2)
cv2.imshow("blurred image3", blur3)
cv2.imshow("edge detected image", canny)    
cv2.waitKey(0)
cv2.destroyAllWindows()