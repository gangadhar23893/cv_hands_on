import cv2
from ultralytics import YOLO

img = cv2.imread("comb_2.jpg")
model = YOLO('yolov8n.pt')

results = model(img,conf=0.05)

annotatd_img = results[0].plot()


cv2.imshow("anntated_image",annotatd_img)
cv2.waitKey(0)
cv2.destroyAllWindows()