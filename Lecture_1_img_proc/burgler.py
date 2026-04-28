import cv2

cap = cv2.VideoCapture(0)

frames = []
gap =5
count =0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frames.append(gray)
    if len(frames) > gap+1:
        frames.pop(0)
        count += 1
    cv2.putText(frame, f"Frames count:{count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if len(frames)>gap:
        diff = cv2.absdiff(frames[0],frames[-1])
        _,thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) < 5000:
                continue
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        motion = any(cv2.contourArea(contour) >= 5000 for contour in contours)
        if motion:
            cv2.putText(frame, "Motion Detected", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imwrite(f'motion_{count}.jpg', frame)
            print(f"Motion detected! Saved frame as motion_{count}.jpg")

    cv2.imshow('frame', frame)
    count += 1
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

