# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:48:09 2019

@author: ppxrv
"""
#SmaractGUI
import serial
from tkinter import *
top = Tk()
top.title('Smaract Control')

def upClk():
    print("+Y step")
    Smar = serial.Serial('COM11',115200); # Open the Port and Specify the Baudrate
    Smar.timeout=(2)
    steps = -1*int(Stps.get())
    amplitude = int(Ss.get())
    frequency = int(Fr.get())
    send = ':MST0,{},{},{}\012'.format(steps,amplitude,frequency)
    Smar.flush()
    Smar.write(send.encode()) # Send the command to the device 
    print(Smar.readline())      #Print return string - (E0,0 for no errors)
    Smar.close()    
def dnClk():
    print("-Y step")
    Smar = serial.Serial('COM11',115200); # Open the Port and Specify the Baudrate
    Smar.timeout=(2)
    steps = int(Stps.get())
    amplitude = int(Ss.get())
    frequency = int(Fr.get())
    send = ':MST0,{},{},{}\012'.format(steps,amplitude,frequency)
    Smar.flush()
    Smar.write(send.encode()) # Send the command to the device 
    print(Smar.readline())      #Print return string - (E0,0 for no errors)
    Smar.close()
 
def twdClk():
    print("-Z step")
    Smar = serial.Serial('COM5',115200); # Open the Port and Specify the Baudrate
    Smar.timeout=(2)
    steps = -1*int(Stps.get())
    amplitude = int(Ss.get())
    frequency = int(Fr.get())
    send = ':MST0,{},{},{}\012'.format(steps,amplitude,frequency)
    Smar.flush()
    Smar.write(send.encode()) # Send the command to the device 
    print(Smar.readline())      #Print return string - (E0,0 for no errors)
    Smar.close()  
def awyClk():
    print("+Z step")
    Smar = serial.Serial('COM5',115200); # Open the Port and Specify the Baudrate
    Smar.timeout=(2)
    steps = int(Stps.get())
    amplitude = int(Ss.get())
    frequency = int(Fr.get())
    send = ':MST0,{},{},{}\012'.format(steps,amplitude,frequency)
    Smar.flush()
    Smar.write(send.encode()) # Send the command to the device 
    print(Smar.readline())      #Print return string - (E0,0 for no errors)
    Smar.close()
    
def lftClk():
    print("-X step")
    Smar = serial.Serial('COM12',115200); # Open the Port and Specify the Baudrate
    Smar.timeout=(2)
    steps = -1*int(Stps.get())
    amplitude = int(Ss.get())
    frequency = int(Fr.get())
    send = ':MST0,{},{},{}\012'.format(steps,amplitude,frequency)
    Smar.flush()
    Smar.write(send.encode()) # Send the command to the device 
    print(Smar.readline())      #Print return string - (E0,0 for no errors)
    Smar.close()    
def rgtClk():
    print("+X step")
    Smar = serial.Serial('COM12',115200); # Open the Port and Specify the Baudrate
    Smar.timeout=(2)
    steps = int(Stps.get())
    amplitude = int(Ss.get())
    frequency = int(Fr.get())
    send = ':MST0,{},{},{}\012'.format(steps,amplitude,frequency)
    Smar.flush()
    Smar.write(send.encode()) # Send the command to the device 
    print(Smar.readline())      #Print return string - (E0,0 for no errors)
    Smar.close()
    
def XID():
    print("X ID")
    Smar = serial.Serial('COM12',115200); # Open the Port and Specify the Baudrate
    Smar.timeout=(2)
    Smar.flush()
    Smar.write(':GSI\012'.encode())  #Get stage/axis IDno.
    print(Smar.readline())          #Print return string
    Smar.close()
def YID():
    print("Y ID")
    Smar = serial.Serial('COM5',115200); # Open the Port and Specify the Baudrate
    Smar.timeout=(2)
    Smar.flush()
    Smar.write(':GSI\012'.encode())  #Get stage/axis IDno.
    print(Smar.readline())          #Print return string
    Smar.close()
def ZID():
    print("Z ID")
    Smar = serial.Serial('COM11',115200); # Open the Port and Specify the Baudrate
    Smar.timeout=(2)
    Smar.flush()
    Smar.write(':GSI\012'.encode())  #Get stage/axis IDno.
    print(Smar.readline())          #Print return string
    Smar.close()

def Stop():
    print("Emergency Stop!")
    Smar = serial.Serial('COM11',115200); # Open the Port and Specify the Baudrate
    Smar.timeout=(2)
    Smar.flush()
    Smar.write(':S0\012'.encode())  #Stop.
    print(Smar.readline())          #Print return string
    Smar.close()

L1 = Label(top, text="Number of steps")                         #Number of steps
L1.pack()
L1.place(bordermode=OUTSIDE,height=25, width=90, x=0, y=30)
Stps = Entry(top, bd =5,textvariable=StringVar(top,'10'))
Stps.pack()
Stps.place(bordermode=OUTSIDE,height=25, width=90, x=95, y=30)

L2 = Label(top, text="Step size")                               #Step size
L2.pack()
L2.place(bordermode=OUTSIDE,height=25, width=90, x=0, y=0)
Ss = Entry(top, bd =5,textvariable=StringVar(top,'2000'))
Ss.pack()
Ss.place(bordermode=OUTSIDE,height=25, width=90, x=95, y=0)

L3 = Label(top, text="Frequency")                               #Frequency
L3.pack()
L3.place(bordermode=OUTSIDE,height=25, width=90, x=0, y=60)
Fr = Entry(top, bd =5,textvariable=StringVar(top,'200'))
Fr.pack()
Fr.place(bordermode=OUTSIDE,height=25, width=90, x=95, y=60)

up=Button(top,text="Up", command = upClk)                       #Up and down
up.pack()
up.place(bordermode=OUTSIDE,height=25, width=90, x=0, y=90)
dn=Button(top,text="Down", command = dnClk)
dn.pack()
dn.place(bordermode=OUTSIDE,height=25, width=90, x=95, y=90)

twd=Button(top,text="Towards", command = twdClk)                #Towards and away
twd.pack()
twd.place(bordermode=OUTSIDE,height=25, width=90, x=0, y=150)
awy=Button(top,text="Away", command = awyClk)
awy.pack()
awy.place(bordermode=OUTSIDE,height=25, width=90, x=95, y=150)

lft=Button(top,text="Left", command = lftClk)                   #Left and right
lft.pack()
lft.place(bordermode=OUTSIDE,height=25, width=90, x=0, y=120)
rgt=Button(top,text="Right", command = rgtClk)
rgt.pack()
rgt.place(bordermode=OUTSIDE,height=25, width=90, x=95, y=120)

xid=Button(top,text="X ID", command = XID)                      #Stage ID's
xid.pack()
xid.place(bordermode=OUTSIDE,height=25, width=55, x=5, y=180)
yid=Button(top,text="Y ID", command = YID)
yid.pack()
yid.place(bordermode=OUTSIDE,height=25, width=55, x=65, y=180)
zid=Button(top,text="Z ID", command = ZID)
zid.pack()
zid.place(bordermode=OUTSIDE,height=25, width=55, x=125, y=180)

Stp=Button(top,text="STOP", command = Stop)
Stp.pack()
Stp.place(bordermode=OUTSIDE,height=25, width=175, x=5, y=210)

top.mainloop()

