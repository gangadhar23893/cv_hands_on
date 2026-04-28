import cv2


cap = cv2.VideoCapture(0)

frames=[]
gap=5
count=0

while True:
    ret,frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frames.append(gray)
    if len(frames)>gap+1:
        frames.pop(0)
    cv2.putText(gray,f"Frame count:{count}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    if len(frames)>gap:
        diff = cv2.absdiff(frames[0],frames[-1])
        _,thresh = cv2.threshold(diff,30,255,cv2.THRESH_BINARY)
        contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if cv2.contourArea(c)<50000:
                continue
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            motion = any(cv2.contourArea(c)>50000 for c in contours)
            if motion:
                cv2.putText(frame,"motion detected",(10,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                cv2.imwrite(f"Motion_frame_{count}.jpg",frame)
                print(f"saved motion detected image")
    cv2.imshow(f"Frame:",frame)
    count+=1

    if cv2.waitKey(1) & 0xff ==27:
        break
cap.release()
cv2.destroyAllWindows()