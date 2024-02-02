#egyszerű pong játék
#Start: 2024.01.31
#Holczer Zoltán

from tkinter import *

jatekHatter="lightgray"

win=Tk()
win.geometry("600x600+100+20")
win.title("Pong játék 10.B/1, 2024")
canvas=Canvas(win,bg=jatekHatter)
canvas.pack(fill=BOTH, expand=1)

canvas.create_arc(0,0,100,100,fill="red")
win.mainloop()