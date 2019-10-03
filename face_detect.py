from imutils import face_utils
import dlib
import cv2
from imutils.video import VideoStream
import imutils
import time

detector = dlib.get_frontal_face_detector()

print("->Starting Face Detection")
c = VideoStream(src=1).start()         		 #For webcam, comment it if using Raspberry Pi Camera module 
#c = VideoStream(usePiCamera=True).start()       #For Raspberry Pi Camera module, comment it if using webcam
time.sleep(2.0)

while True:

    frame = c.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)

    for rect in rects:
        x1 = rect.left()
        y1 = rect.top()
        x2 = rect.right()
        y2 = rect.bottom()
        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (255, 0, 0), 2)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
c.stop()
