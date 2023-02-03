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

root = Tk()
root.title('Incubadora')
root['background'] = 'light green'


def clicked(value):
    {
        print(value)
    }


counter = 0


def counter_label(label):
    def count():
        global counter
        counter += 1
        texto = str(counter)+'%'
        label.config(text=texto)
        label.after(1000, count)
    count()


counter2 = 0


def counter_label2(label):
    def count2():
        global counter2
        counter2 += 1
        texto2 = str(counter2)+' grados'
        label.config(text=texto2)
        label.after(1000, count2)
    count2()


titulo = Label(root, text="Interfaz Python",
               font="Roboto 16 bold", width=15, bg='light green')
etiqueta1 = Label(root, text="Configuración de",
                  font="Roboto 14", width=17, anchor=SW, bg='light green')
etiqueta2 = Label(root, text="iluminación máx. o min",
                  font="Roboto 14", width=17, anchor=NW, bg='light green')
etiqueta3 = Label(root, text="Estado de iluminación:",
                  font="Roboto 14", width=17, anchor=W, bg='light green')
etiqueta4 = Label(root, text="Ángulo de motor:",
                  font="Roboto 14", width=17, anchor=W, bg='light green')

ilumMax = Label(root, font="Roboto 14",
                bg="yellow", width=10, borderwidth=5)
ilumMin = Label(root, text="40%", font="Roboto 14",
                bg="yellow", width=10, borderwidth=5)

ilumState = Label(root, text="87%", font="Roboto 14",
                  bg="cyan", width=10, borderwidth=5)
angState = Label(root, text="30 Grados", font="Roboto 14",
                 bg="cyan", width=12, borderwidth=5)

r = IntVar()
r.set(1)
check1 = Radiobutton(root, text="Potenciómetro", font="Roboto 14", width=15, indicatoron=0,
                     variable=r, value=0, command=lambda: clicked(r.get()), anchor=W)
check2 = Radiobutton(root, text="Slider", font="Roboto 14", width=15, indicatoron=0,
                     variable=r, value=1, command=lambda: clicked(r.get()), anchor=W)
slider1 = Scale(root, from_=0, to=120,  length=300,
                border=2, orient=HORIZONTAL)

titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
etiqueta1 .grid(row=1, column=0, padx=10, pady=0, sticky=S)
etiqueta2 .grid(row=2, column=0, padx=10, pady=0, sticky=N)
etiqueta3 .grid(row=3, column=0, padx=10, pady=10)
etiqueta4 .grid(row=4, column=0, padx=10, pady=10)

ilumMax.grid(row=1, column=1, padx=10, pady=2, sticky=W)
ilumMin.grid(row=2, column=1, padx=10, pady=2, sticky=W)
ilumState.grid(row=3, column=1, padx=10, pady=10, sticky=W)
angState.grid(row=4, column=1, padx=10, pady=10, sticky=W)

check1.grid(row=5, column=0, padx=10, pady=2, sticky=E)
check2.grid(row=6, column=0, padx=10, pady=2, sticky=E)

slider1.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

counter_label(ilumMax)
counter_label(ilumMin)
counter_label(ilumState)
counter_label2(angState)

check1.deselect()
check2.select()

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
