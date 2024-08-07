#library import
# object of VideoCapture class
#use it inside a while loop
import os
import cv2
import sys

path= r"C:\Users\Eishta Singh\Videos\Captures\UnifiedShareSheet.mp4"
if not os.path.exists(path):
    print(f"Filenotfound: {path}")
    sys.exit(1)

cam=cv2.VideoCapture(path)
while True:
    state, frame =cam.read()
    if not state:
        break
    #resize
    frame1=cv2.resize(frame,(500,500))
    frame2=cv2.resize(frame,(0,0),fx=.5, fy=.5)
    cv2.imshow("Video Residzed", frame1)
    cv2.imshow("Video Residzed by scale", frame2)
    if cv2.waitKey(10) == ord('q'):
        break