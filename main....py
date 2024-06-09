from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox 

import cv2
from PIL import Image
from PIL import ImageTk
from scipy.spatial import distance as dist
import numpy as np
import serial
import time 
import os



with open('coco.names', 'r') as f:
    classes = f.read().splitlines()
net = cv2.dnn.readNetFromDarknet('yolov4.cfg', 'yolov4.weights')
model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale=1/255, size=(416, 416), swapRB=True)

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("http://100.68.22.87:8080/video")
def Start():
    global cap

    ij, frame = cap.read()

    classIds, scores, boxes = model.detect(frame, confThreshold=0.6, nmsThreshold=0.4)
    if len(classIds) > 0: 
        for (classId, score, box) in zip(classIds, scores, boxes):
            cv2.rectangle(frame, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), color=(0, 255, 0), thickness=2)
            text = classes[classId]
            e1.delete(0,END)
            e1.insert(0,str(text))
            if(text=="stop sign"):
                print("Stop")
                port="COM5"
                bluetooth=serial.Serial(port, 9600)
                bluetooth.flushInput()
                bluetooth.write(b"Stop00")
                bluetooth.close()
                time.sleep(1)
            if(text=="traffic light"):
                print("start")
                port="COM5"
                bluetooth=serial.Serial(port, 9600)
                bluetooth.flushInput()
                bluetooth.write(b"ena110")
                bluetooth.close()
                time.sleep(1)
                port="COM5"
                bluetooth=serial.Serial(port, 9600)
                bluetooth.flushInput()
                bluetooth.write(b"Front0")
                bluetooth.close()
                time.sleep(1)
    else:
        print("go")


    if ij==1:
        img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        resized_image = cv2.resize(img,(650,550))    
        image = Image.fromarray(resized_image)
        image = ImageTk.PhotoImage(image)
        panelA = Label(image=image)
        panelA.image = image
        panelA.place(x=628 ,y=120)
        panelA.after(2, Start)
    else:
        return

def Front_normal():
    port="COM5"
    bluetooth=serial.Serial(port, 9600)
    bluetooth.flushInput()
    bluetooth.write(b"ena110")
    bluetooth.close()
    time.sleep(1)

    port="COM5"
    bluetooth=serial.Serial(port, 9600)
    bluetooth.flushInput()
    bluetooth.write(b"Front0")
    bluetooth.close()
    time.sleep(1)

def Right():
    port="COM5"
    bluetooth=serial.Serial(port, 9600)
    bluetooth.flushInput()
    bluetooth.write(b"ena110")
    bluetooth.close()
    time.sleep(1)

    port="COM5"
    bluetooth=serial.Serial(port, 9600)
    bluetooth.flushInput()
    bluetooth.write(b"Right0")
    bluetooth.close()
    time.sleep(1)


def  Left():
    port="COM5"
    bluetooth=serial.Serial(port, 9600)
    bluetooth.flushInput()
    bluetooth.write(b"ena110")
    bluetooth.close()
    time.sleep(1)

    port="COM5"
    bluetooth=serial.Serial(port, 9600)
    bluetooth.flushInput()
    bluetooth.write(b"Left00")
    bluetooth.close()
    time.sleep(1)

def Back():
    port="COM5"
    bluetooth=serial.Serial(port, 9600)
    bluetooth.flushInput()
    bluetooth.write(b"ena110")
    bluetooth.close()
    time.sleep(1)

    port="COM5"
    bluetooth=serial.Serial(port, 9600)
    bluetooth.flushInput()
    bluetooth.write(b"Back00")
    bluetooth.close()
    time.sleep(1)


def Stop():
    port="COM5"
    bluetooth=serial.Serial(port, 9600)
    bluetooth.flushInput()
    bluetooth.write(b"ena110")
    bluetooth.close()
    time.sleep(1)

    port="COM5"
    bluetooth=serial.Serial(port, 9600)
    bluetooth.flushInput()
    bluetooth.write(b"Stop00")
    bluetooth.close()
    time.sleep(1)

    root.destroy()


      
root = Tk() 
root.title('SELF DRIVING CAR')
root.geometry('1920x1080')
root.configure(background='lightgray')


c1 = Canvas(root,bg='lightgray',width=1860,height=80)
c1.place(x=20,y=20)
l1=Label(root,text='SELF DRIVING CAR',foreground="red",background='lightgray',font =('Verdana',20))
l1.place(x=850,y=40)



c2 = Canvas(root,bg='white',width=650,height=550) 
c2.place(x=628,y=120)
lmain = Label(root,bg='white')
lmain.place(x=628,y=120)


c3 = Canvas(root,bg='lightgray',width=1860,height=80) 
c3.place(x=20,y=700)

b0=Button(root,borderwidth=1,relief="flat",text ="FRONT AI",font="verdana 12 bold",bg="white",fg="red",command = Start)
b0.place(height=50,width=150,x=100,y=715)

b1=Button(root,borderwidth=1,relief="flat",text ="FRONT NORMAL",font="verdana 12 bold",bg="white",fg="red",command = Front_normal)
b1.place(height=50,width=150,x=300,y=715)

b2=Button(root,borderwidth=1,relief="flat",text ="BACK",font="verdana 12 bold",bg="white",fg="red",command = Back)
b2.place(height=50,width=150,x=560,y=715)

var1=StringVar()
e1=Entry(root,textvariable=var1,font=('Verdana',12,'bold'),foreground='RED',justify=LEFT)
e1.place(height=50,width=200,x=850,y=715)

b3=Button(root,borderwidth=1,relief="flat",text ="RIGHT",font="verdana 12 bold",bg="white",fg="red",command = Right)
b3.place(height=50,width=150,x=1100,y=715)

b4=Button(root,borderwidth=1,relief="flat",text ="LEFT",font="verdana 12 bold",bg="white",fg="red",command = Left)
b4.place(height=50,width=150,x=1350,y=715)

b5=Button(root,borderwidth=1,relief="flat",text ="STOP",font="verdana 12 bold",bg="white",fg="red",command = Stop)
b5.place(height=50,width=150,x=1600,y=715)


mainloop()

