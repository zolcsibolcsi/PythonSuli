import random
import math

def veletlen(mettol, meddig, lepes=1):
    darab=math.ceil((meddig-mettol)/lepes)
    eltolas=mettol

    szam=math.floor(random.random()*darab)*lepes+eltolas
    return szam

print(veletlen(10,20))   

szamok=[]
for i in range(100):
    szamok.append(veletlen(10,20))

print(szamok)

veletlen(160,200)

lista=[]
for i in range(0,veletlen(10,21)):
    belso=[]
    for a in range(1,veletlen(10,21)):
        belso.append(veletlen(160,201))
    lista.append(belso)

for i,elem in enumerate (lista):
    print(i,":", elem)

szamok=[[veletlen(160,200) for _ in range(veletlen(10,21))] for _ in range(veletlen(10,200))]