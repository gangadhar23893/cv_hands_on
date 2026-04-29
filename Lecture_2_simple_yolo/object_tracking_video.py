import cv2
from ultralytics import YOLO
import numpy as np

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(r"/Users/gangadhar/Documents/my_folder/my_projects/Cv_hands_on/8720278-uhd_3840_2160_25fps.mp4")
unique_ids = set()
while True:
    ret,frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (1280, 720))
    results = model.track(frame,persist=True)
    annotated_frame = results[0].plot()
    if results[0].boxes and results[0].boxes.id is not None:
        #ids = results[0].boxes.id.numpy(0)
        ids = results[0].boxes.id.int().cpu().tolist()

        for oid in ids:
            unique_ids.add(oid)
        cv2.putText(annotated_frame,f"count:{len(unique_ids)}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.imshow("Object tracking",annotated_frame)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
