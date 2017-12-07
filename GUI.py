from Tkinter import *
import time,os,cv2

class GUI(Frame):

    def register_countdown(self):
        self.LABEL["text"] = "Coloquese frente a la camara, a unos 30 cm"

        self.LABEL_COUNTDOWN.after(2000,lambda: self.LABEL_COUNTDOWN.config(text='3'))
        self.LABEL_COUNTDOWN.after(3000,lambda: self.LABEL_COUNTDOWN.config(text='2'))
        self.LABEL_COUNTDOWN.after(4000,lambda: self.LABEL_COUNTDOWN.config(text='1'))
        self.LABEL_COUNTDOWN.after(5000,lambda: self.register())
        
    def train(self):
        os.system('/usr/bin/python modules/trainer.py')
        

    def register(self):
        
        cam = cv2.VideoCapture(0)
        detector=cv2.CascadeClassifier('Classifiers/lbpcascade_frontalface_improved.xml')
        i=0
        offset=50
        name=self.USER_ENTRY.get()
        newid = 1
        with open("DB/idlist.txt",'r') as reader:
            for l in reader:
                newid = newid + 1
                
        print('new id: '+str(newid))
        idlist_file = open('DB/idlist.txt','a')
        idlist_file.write(str(newid) + ' ' + name + '\n')
        idlist_file.close()

        while True:
            ret, im =cam.read()
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
            for(x,y,w,h) in faces:
                i=i+1
                cv2.imwrite("dataSet/face-"+str(newid) +'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
                cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
                cv2.imshow('im',im[y-offset:y+h+offset,x-offset:x+w+offset])
                cv2.waitKey(100)
            if i>50:
                cam.release()
                cv2.destroyAllWindows()
                break
            
#        train()
        os.system('/usr/bin/python modules/trainer.py')

    
    def createWidgets(self):
        
        
        self.LABEL = Label(self)
        self.LABEL.pack({"side":"top"})
        
        self.LABEL_COUNTDOWN = Label(self)
        self.LABEL_COUNTDOWN["fg"] = "red"
        self.LABEL_COUNTDOWN.pack({"side":"bottom"})
        
        
        
        self.LABEL["text"] = "Introduzca su nombre:"
        self.USER_ENTRY = Entry(self,bd=10)
        self.USER_ENTRY.pack({"side":"top"})
        self.USER_ENTRY.focus_set()
        self.USER_BTN = Button(self,height=10, width=30)
        self.USER_BTN["text"] = "Aceptar"
        self.USER_BTN.pack({"side":"bottom"})
        self.USER_BTN["command"] = self.register_countdown

        
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
        
root = Tk()

#root.overrideredirect(True)
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))

app = GUI(master=root)

app.mainloop()
root.destroy()