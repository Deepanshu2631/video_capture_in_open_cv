import cv2
cap = cv2.VideoCapture(0)#capture video and store in variable
#we can get the default webcam resolution using get method
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HRIGHT))
    # but we can set the max resolution using set method
cap.set(3,1280)
cap.set(4,720)
while(True):# run continuously
    ret ,  frame = cap.read()# read capture data form cap to frame

    cv2.imshow('frame' ,  frame)#show frame
    if cv2.waitKey(1) & 0XFF ==  ord('q'):
        #when q will pressed clos loop and quit window
        break
cap.release()
cv2.destroyAllWindows()
