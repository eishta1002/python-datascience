import cv2

path =r"C:\Users\Eishta Singh\Downloads\VID-20240718-WA0013.mp4"
video =cv2.VideoCapture(path)

while True:
    state ,frame =video.read()
    if not state :break
    frame=cv2.resize(frame, (0,0), fx=.25,fy=.25)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)

    #stacking frame
    s1= cv2.hconcat([frame, cv2.merge([gray,gray ,gray])])
    s2= cv2.hconcat([rgb, hsv])
    f = cv2.vconcat([s1,s2])
    h, W,_ = f.shape
    #adding text
    cv2.putText(f, "Original", (50,50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2)
    cv2.putText(f, "Grayscale", (W//2 +50,50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,255),5)
    cv2.putText(f, "RGB", (50,h//2+100), 
                cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,255),2)
    cv2.putText(f, "HSV", (W//2+50, h//2+100), 
                cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,255),2)
    
    cv2.imshow('frame', f)
    
    
    if cv2.waitKey(10)==ord('q'):
        break
