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


fenyo2=[0,0,
        200,0,
        100,200,
        200,200,
        200,250,
        0,250,
        115,50,
        0,50,
        0,0
        ]

fenyo2Masolat=transzformaciok.eltol(fenyo2,100,100)
canvas.create_line(fenyo2,width=5,fill="green")


win.mainloop()