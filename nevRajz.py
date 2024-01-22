import transzformaciok
from tkinter import *

#ablak létrehozása
win=Tk()

#ablak mérete
win.geometry("600x600")

#canvas létrehozás
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")
#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)


zoli=[0,0,
        200,0,
        100,200,
        200,200,
        200,250,
        0,250,
        115,50,
        0,50,
        0,0
        ],#Z

zoli=[x.extend(x[:2]) for x in zoli]

zoli2=[]
for e in zoli:
    e=transzformaciok.nagyit(e,10)
    e=transzformaciok.eltol(e,100,100)
    e=transzformaciok.forgat(e,45)

    zoli2.append(e)


for e in zoli2:
    canvas.create_line(e,width=2,fill="red")

canvas.create_line(zoli[0],width=5,fill="red")
fenyo2Masolat=transzformaciok.eltol(zoli,100,100)
canvas.create_line(zoli,width=5,fill="green")


win.mainloop()