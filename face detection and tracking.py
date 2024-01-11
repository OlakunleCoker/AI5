import cv2

alg = "C:/Users/OWNER/Desktop/AI PS/AI5/haarcascade_frontalface_alt.xml"

haar_cascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture(0)

while True:
    _,img = cam.read()#getting the camera frame
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),2)#Drawing rectangle  
    cv2.imshow("FaceDetection",img)
    key = cv2.waitKey(10)#pressing the escape button to terminate the code
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()
        
        
