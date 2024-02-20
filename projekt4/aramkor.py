#Áramkör
#Start: 2024.02.16
#Holczer Zoltán

from tkinter import *
import random

class jel:
	x = 0
	y = 0
	meret = 100
	szin="black"
	r=meret*0.06
	def __init__(self,x,y,meret,canvas):
				self.x=x
				self.y=y
				self.meret=meret
				self.canvas=canvas
				self.rajz()


	def rajz(self, vonal=[]):
			self.canvas.create_rectangle(self.x, self.y, self.x+self.meret, self.y+self.meret, fill="blue")

			for egyvonal in vonal:
						self.canvas.create_line(egyvonal, width=self.meret*0.03, fill=self.szin)


class elem(jel):
			def rajz(self):
					vonal=[
						[
								self.x,self.y+self.meret*0.5,
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
						],
					]
					jel.rajz(self,vonal=vonal)

class kapcsolo(jel):
			def rajz(self):
					vonal=[
						[
								self.x,self.y+self.meret*0.5,
								self.x+self.meret*0.333-self.r, self.y+self.meret*0.5,
						],
						[
								self.x+self.meret*0.333+self.r, self.y+self.meret*0.5,
								self.x+self.meret*0.45, self.y+self.meret*0.8,
						],
						[
								self.x+self.meret*0.666+self.r, self.y+self.meret*0.5,
								self.x+self.meret, self.y+self.meret*0.5,
						],
					]
					jel.rajz(self,vonal=vonal)
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

elem1=elem(200,200,100,canvas)
elem1.rajz()

kapcsolo1=kapcsolo(400,350,100,canvas)

win.mainloop()