class Emlos:
	lab=4
	def __init__(self):
		self.suly=0

	def beszel(self):
		pass

class Macska(Emlos):
	def __init__(self,nev):
		super().__init__()
		self.nev=nev
		self.suly=1
	
	def beszel(self):
		print("Miaú!")


emlos1=Emlos()
emlos1.beszel()

macska1=Macska("Sutike")
macska1.beszel()
print(macska1.suly,macska1.nev)


#hf: egy masik macskat csinalni, legalabb egy fajta aminek adunk meg tulajdonsagokat es még fuggvenyt(szin,magassag,cselekves[seta,karmolas,lopakodas])