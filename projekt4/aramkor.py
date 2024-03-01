#Áramkör
#Start: 2024.02.16
#Török Ádám

from tkinter import *
import random
import math
class Jel:
    x = 0
    y = 0
    meret = 100
    szin="black"

    def __init__(self,x,y,meret,canvas):
        self.x=x
        self.y=y
        self.meret=meret
        self.r=self.meret*0.06
        #bekötési pont
        self.bkp=[[self.x, self.y+self.meret*0.5], [self.x+self.meret, self.y+self.meret*0.5]]
        self.canvas=canvas
        self.rajz()



    def rajz(self, vonalak=[],korok=[]):
        self.canvas.create_rectangle(self.x, self.y, self.x+self.meret, self.y+self.meret, fill="grey")

        for egyvonal in vonalak:
            self.canvas.create_line(egyvonal, width=self.meret*0.03, fill=self.szin)
        for egykor in korok:
            self.canvas.create_oval(egykor, outline=self.szin, width=self.meret*0.03)

    def vezetek(self,masik, sajatBKP=1, masikBKP=0):
    
        if sajatBKP==1 and masikBKP==0 and self.bkp[sajatBKP][0] < masik.bkp[masikBKP][0]:
            vonalak=[
                [
                    self.bkp[sajatBKP][0], self.bkp[sajatBKP][1],
                    (self.bkp[sajatBKP][0]+masik.bkp[masikBKP][0])/2, self.bkp[sajatBKP][1],
                    (self.bkp[sajatBKP][0]+masik.bkp[masikBKP][0])/2, masik.bkp[masikBKP][1],
                    masik.bkp[masikBKP][0], masik.bkp[masikBKP][1],
                ],
            ]
        elif sajatBKP==1 and masikBKP==1 and self.bkp[sajatBKP][0] < masik.bkp[masikBKP][0]:
            vonalak=[
                [
                    self.bkp[sajatBKP][0], self.bkp[sajatBKP][1],
                    (self.bkp[sajatBKP][0]+masik.x)/2, self.bkp[sajatBKP][1],
                    (self.bkp[sajatBKP][0]+masik.x)/2, masik.y+masik.meret*1.2,
                    masik.x+masik.meret*1.2,                            masik.y+masik.meret*1.2,
                    masik.x+masik.meret*1.2,                            masik.bkp[masikBKP][1],
                    masik.bkp[masikBKP][0], masik.bkp[masikBKP][1],
                ],
            ]
        else:
            vonalak=[
                [
                    self.bkp[sajatBKP][0], self.bkp[sajatBKP][1],
                    (self.bkp[sajatBKP][0]+masik.bkp[masikBKP][0])/2, self.bkp[sajatBKP][1],
                    (self.bkp[sajatBKP][0]+masik.bkp[masikBKP][0])/2, masik.bkp[masikBKP][1],
                    masik.bkp[masikBKP][0], masik.bkp[masikBKP][1],
                ],
            ]
    
        for egyvonal in vonalak:
            self.canvas.create_line(egyvonal, width=self.meret*0.03, fill=self.szin)

class Elem(Jel):
    def rajz(self):
        vonalak=[
            [
                self.x, self.y+self.meret*0.5,
                self.x+self.meret*0.45, self.y+self.meret*0.5,
            ],
            [
                self.x+self.meret*0.45, self.y+self.meret*0.2,
                self.x+self.meret*0.45, self.y+self.meret*0.8,
            ],
            [
                self.x+self.meret*0.55, self.y+self.meret*0.4,
                self.x+self.meret*0.55, self.y+self.meret*0.6,
            ],
            [
                self.x+self.meret*0.55, self.y+self.meret*0.5,
                self.x+self.meret, self.y+self.meret*0.5,
            ]
        ]
        Jel.rajz(self,vonalak)

class Kapcsolo(Jel):
    def rajz(self):
        vonalak=[
            [
                self.x, self.y+self.meret*0.5,
                self.x+self.meret*0.333-self.r, self.y+self.meret*0.5,
            ],
            [
                self.x+self.meret*0.333+self.r, self.y+self.meret*0.5,
                self.x+self.meret*0.666-self.r, self.y+self.meret*0.3,
            ],
            [
                self.x+self.meret*0.666+self.r, self.y+self.meret*0.5,
                self.x+self.meret, self.y+self.meret*0.5,
            ]
        ]
        korok=[
            [
                self.x+self.meret*0.333-self.r, self.y+self.meret*0.5-self.r,
                self.x+self.meret*0.333+self.r, self.y+self.meret*0.5+self.r
            ],
            [
                self.x+self.meret*0.666-self.r, self.y+self.meret*0.5-self.r,
                self.x+self.meret*0.666+self.r, self.y+self.meret*0.5+self.r
            ]
        ]
        Jel.rajz(self,vonalak,korok)

class Lampa(Jel):
    def rajz(self):
        dx=self.r/math.sqrt(2)
        self.r=self.meret*0.25
        vonalak=[
            [
                self.x, self.y+self.meret*0.5,
                self.x+self.meret*0.5-self.r, self.y+self.meret*0.5,
            ],
            [
                self.x+self.meret*0.5-dx, self.y+self.meret*0.5-dx,
                self.x+self.meret*0.5+dx, self.y+self.meret*0.5+dx,
            ],
            [
                self.x+self.meret*0.5-dx, self.y+self.meret*0.5+dx,
                self.x+self.meret*0.5+dx, self.y+self.meret*0.5-dx,
            ],
            [
                self.x+self.meret*0.5+self.r, self.y+self.meret*0.5,
                self.x+self.meret, self.y+self.meret*0.5,
            ]
        ]
        korok=[
            [
                self.x+self.meret*0.5-self.r, self.y+self.meret*0.5-self.r,
                self.x+self.meret*0.5+self.r, self.y+self.meret*0.5+self.r
            ],
        ]
        Jel.rajz(self,vonalak,korok)

class Ellenallas(Jel):
    def rajz(self):
        
        vonalak=[
            [
                self.x, self.y+self.meret*0.5,
                self.x+self.meret*0.25, self.y+self.meret*0.5,
            ],
            [
                self.x+self.meret*0.25, self.y+self.meret*0.4,
                self.x+self.meret*0.25, self.y+self.meret*0.7,
                self.x+self.meret*0.75, self.y+self.meret*0.7,
                self.x+self.meret*0.75, self.y+self.meret*0.4,
                self.x+self.meret*0.25, self.y+self.meret*0.4,
            ],
            [
                self.x+self.meret*0.75, self.y+self.meret*0.5,
                self.x+self.meret*1.0, self.y+self.meret*0.5,
            ],
        ]
        Jel.rajz(self,vonalak)
#ablak létrehozása
win=Tk()

jatekHatter="lightgray"
jatekSpeed=10

#ablak mérete
win.geometry("1000x600")

win.title("Áramkör")

#canvas létrehozás
canvas=Canvas(win, width=600, height=600, bg=jatekHatter)

#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)

elem1=Elem(100,100,100,canvas)
#elem1.rajz()
kapcsolo1=Kapcsolo(750,200,100,canvas)

lampa1=Lampa(10,10,100,canvas)
lampa1.rajz()

kapcsolo1.vezetek(elem1, masikBKP=1)
lampa1.vezetek(kapcsolo1,masikBKP=1)

Ellenallas1=Ellenallas(400,100,100,canvas)
win.mainloop()