import cv2
import time


cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('./Classifiers/lbpcascade_frontalface_improved.xml')
i=0
offset=50
name=raw_input('Ingresa tu nombre: ')
newid = 1
with open("./DB/idlist.txt",'r') as reader:
    for l in reader:
        newid = newid + 1
        
print('new id: '+str(newid))
idlist_file = open('./DB/idlist.txt','a')
idlist_file.write(str(newid) + ' ' + name + '\n')
idlist_file.close()

while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        i=i+1
        cv2.imwrite("./dataSet/face-"+str(newid) +'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        cv2.imshow('im',im[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.waitKey(100)
    if i>50:
        cam.release()
        cv2.destroyAllWindows()
        break

