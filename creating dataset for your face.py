import cv2
import os#helpful to create/check directories
dataset = "dataset"#dataset to created in my local directory
name = "yetty"

path = os.path.join(dataset,name)#it will dataset/yetty
if not os.path.isdir(path):# to check the availability of the path or not
    os.mkdir(path)#if it is not there, it will create it

(width,height) = (130,100)
alg = "C:/Users/OWNER/Desktop/AI PS/AI5/haarcascade_frontalface_alt.xml"
haar_cascade = cv2.CascadeClassifier(alg)
cam = cv2.VideoCapture(0)

count = 1
while count < 31: #captures 30 images and close automatically
    print(count)
    _,img = cam.read()
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face: #to capture only the face area
        cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),2)
        faceOnly = grayImg[y:y+h,x:x+w]# face only image
        resizeImg = cv2.resize(faceOnly,(width,height))
        cv2.imwrite("%s/%s.jpg" %(path,count),resizeImg)#saving image in the form of grayscale image and also resize image 
        count+=1
    cv2.imshow("FaceDetection",img)
    key = cv2.waitKey(10)
    if key == 27:
        break
print("Image Captured Successfully")
cam.release()
cv2.destroyAllWindows()
        
        
