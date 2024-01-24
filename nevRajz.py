import transzformaciok
from tkinter import *

#ablak létrehozása
win=Tk()

#ablak mérete
win.geometry("1000x1000")

#canvas létrehozás
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")
#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)

fenyo2=[200,0,
        0,100,
        150,100,
        0,200,
        150,200,
        0,300,
        150,300,
        150,400,
        250,400,
        250,300,
        400,300,
        250,200,
        400,200,
        250,100,
        400,100,
        200,0]

fenyo2Masolat=transzformaciok.eltol(fenyo2,100,100)
#canvas.create_line(fenyo2Masolat,width=5,fill="green")

zoli=[[0,0,
        200,0,
        100,200,
        200,200,
        200,250,
        0,250,
        115,50,
        0,50,
        0,0],

   [0,0,
        200,0,
        100,200,
        200,200,
        200,250,
        0,250,
        115,50,
        0,50,
        0,0]]

"""zoli2=[]
for e in zoli:
        e=transzformaciok.nagyit(e, 2)
        e=transzformaciok.eltol(e, 100, 100)
        e=transzformaciok.forgat(e, 90)
        zoli2.append(e)
"""
zoli2=transzformaciok.forgat(zoli2,0)

print(zoli2)
for e in zoli2:
        canvas.create_line(e,width=5,fill="black")
win.mainloop()
