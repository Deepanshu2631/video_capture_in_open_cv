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
    font  = cv2.FONT_HERSHEY_DUPLEX
    text = 'width' + str(cap.get(3)) +'hieght'+str(cap.get(4))
    frame = cv2.putText(frame , text , (10 , 50) , font , 1, (200, 210, 200), 2 , cv2.LINE_AA)#to print width and hieght in frame
     datet = str(datetime.datetime.now())# for showing live date and time but you have to import datetime
     frame = cv2.putText(frame, datet, (10, 700), font, 1, (200, 210, 200), 2, cv2.LINE_AA)
       
    cv2.imshow('frame' ,  frame)#show frame
    if cv2.waitKey(1) & 0XFF ==  ord('q'):
        #when q will pressed clos loop and quit window
        break
cap.release()
cv2.destroyAllWindows()
