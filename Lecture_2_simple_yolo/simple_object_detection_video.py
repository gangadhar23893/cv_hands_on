import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("16229180-uhd_2160_3840_60fps.mp4")

while True:
    ret,frame=cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (1280, 720))
    results= model(frame,classes=[0])
    annotated_frame = results[0].plot()
    cv2.imshow("annotated_frame",annotated_frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()