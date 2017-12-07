import cv2
import numpy as np
import time

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('../trainer/trainer.yml')
cascadePath = "../Classifiers/lbpcascade_frontalface_improved.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);


cam = cv2.VideoCapture(0)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
##        print('ID: '+str(Id)+' Conf:'+str(conf) + '\n') 
        if(conf<=50):
            found = 0
            with open('../DB/idlist.txt', 'r') as reader:
                for line in reader:
                    idlist = line.split(' ')
                    if(Id==int(idlist[0])):
                        Id=idlist[1][:len(idlist[1])-1]
                        found = 1
                        print("Encontrado")
            if(found == 0):
                Id="Desconocido"
                print("Desconocido")
        else:
            Id="Desconocido"
            print("Desconocido")
        cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
    cv2.imshow('im',im) 
    if cv2.waitKey(10)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
