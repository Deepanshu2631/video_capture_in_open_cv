import cv2
cap = cv2.VideoCapture(0)#capture video and store in variable
while(True):# run continuously
    ret ,  frame = cap.read()# read capture data form cap to frame

    cv2.imshow('frame' ,  frame)#show frame
    if cv2.waitKey(1) & 0XFF ==  ord('q'):
        #when q will pressed clos loop and quit window
        break
cap.release()
cv2.destroyAllWindows()