import threading
from tkinter import *
import tkinter as tk
import serial
root = tk.Tk()
COM = "COM2"
ser = serial.Serial(port=COM, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=2)
ser.isOpen()
msg = ""


# read Serial
def ReadSerial():
    global msg
    msg = ""
    msg = ser.readline()[:-2].decode("utf-8")
    if msg != "":
        print(msg)
        
    return msg
# write Serial
def WriteSerial(sendmsg):
    print("send")
    ser.write(bytes(sendmsg, 'utf-8'))
    ReadSerial()


# Tkinter
root.title("WIP NAME")
root.geometry("650x400")
inputData = Entry(root, text="<Slave1&p>") # input for enter the message to write
entrymsg = inputData.get() # get the massage
buttonMsg = Button(root, text="send", command = lambda: WriteSerial(inputData.get())) # create a send button for send the message
readData = Label(root, text=msg) # show message in Tkinter
ReadSerial()
# show items
inputData.grid()
readData.grid()
buttonMsg.grid()


# GUI thread
def TkinterGui():
    while 1==1:
        global msg
        entrymsg = inputData.get()


# Serial thread
def SerialProgram():
    while 1==1:
        ReadSerial()
        readData.update_idletasks()


x = threading.Thread(target=TkinterGui, args=())
y = threading.Thread(target=SerialProgram, args=())
x.start()
y.start()

root.mainloop()