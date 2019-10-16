import cv2, time, pandas
from datetime import datetime 

video = cv2.VideoCapture(0)

first_frame = None
# status_list initialized with two values due to first iteration before append to avoid list our of range
status_list = [None, None]
times = []
df = pandas.DataFrame(columns=["Start", "End"])

while True: 
    check, frame = video.read()  
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21),0)

    if first_frame is None: 
        first_frame = gray
        continue           

    delta_frame=cv2.absdiff(first_frame, gray)  
    thresh_delta_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]  # returns tuple
    thresh_delta_frame = cv2.dilate(thresh_delta_frame, None, iterations=2)
    (cnts,_) = cv2.findContours(thresh_delta_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000: 
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+y, y+h), (0, 255, 0), 3)
    status_list.append(status)
# clearing list of all besides two last values
    status_list=status_list[-2:]        
# creating start-stop log 
    if status_list[-1] == 1 and status_list[-2] == 0: 
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1: 
        times.append(datetime.now())
        
    cv2.imshow("Window name", delta_frame)
    cv2.imshow("Capture", gray)
    cv2.imshow("Threshold Frame", thresh_delta_frame)
    cv2.imshow("Color frame", frame)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        if status == 1: 
            times.append(datetime.now())                # last show up 
        break

for i in range(0, len(times),2):
    df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows
