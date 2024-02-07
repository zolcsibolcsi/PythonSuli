#egyszerű pong játék
#Start: 2024.01.31
#Holczer Zoltán

from tkinter import *
import random

def rajzol():
    
    labdaPos[0]+=labdaSpeed[0]
    labdaPos[1]+=labdaSpeed[1]

    if labdaPos[0]>win.winfo_width() or labdaPos[0]<0:
        labdaSpeed[0]*=-1
        #labdaColor=randomColor()
    if labdaPos[1]>win.winfo_height() or labdaPos[1]<0:
        labdaSpeed[1]*=-1
        #labdaColor=randomColor()
    labdaLista.append(canvas.create_oval(labdaPos[0],
                       labdaPos[1],
                       labdaPos[0]+labdaSize,
                       labdaPos[1]+labdaSize,
                       fill=labdaColor,outline=""))
    if len(labdaLista)>labdaListaHossz:
        canvas.delete(labdaLista[0])
        labdaLista.pop(0)

    win.after(jatekSpeed,rajzol)

def randomColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return ("#"+hex(r)[-2:]+hex(g)[-2:]+hex(b)[-2:]).replace("x","0")

def atmenetColor(red, green, blue):
    red+=5
    if red>255:
        red=red-255
        green+=5
    if green>255:
        green=green-255
        blue+=5
    if blue>255:
        blue=blue-255

    return ("#"+hex(red)[-2:]+hex(green)[-2:]+hex(blue)[-2:]).replace("x","0"),red,green,blue

    pass
jatekHatter="lightgray"
jatekSpeed=10
print(randomColor())

win=Tk()
win.geometry("600x620+100+20")
win.title("Pong játék 10.B/1, 2024")
canvas=Canvas(win,bg=jatekHatter)
canvas.pack(fill=BOTH, expand=1)

canvas.create_oval(0,0,100,100,fill="red")

labdaSpeed=[5,5.25]
labdaPos=[200,100]
labdaSize=20

labdaColor="red"

red,green,blue=0,0,0


labdaLista=[]
labdaListaHossz=1

win.after(jatekSpeed,rajzol)
win.mainloop()

while True:
    #labdaColor,red,green,blue=atmenetColor(red,green,blue)
    #print(labdaColor)
    rajzol()
    canvas.update()


