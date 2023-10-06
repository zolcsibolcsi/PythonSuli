# Mértékegység átváltó
# Holczer Zoltán 2023.10.06
# Projekt feladat


tipusok=["Hosszúság","Terület","Térfogat","Tömeg","Űrmérték","Űrmérték + térfogat"]
egysegek=[["mm","cm","dm","m","km"],
          ["mm2","cm2","dm2","m2","km2"],
          ["mm3","cm3","dm3","m3","km3"]]

valtok=[[10,10,10,1000,1],
          [100,100,100,1000000,1],
          [1000,1000,1000,1000000000,1]]

print("#"*30)
#for elem in tipusok:
    #print(elem)

for i,elem in enumerate(tipusok):
    print("\t"+str(i+1)+":",elem)

print("\t0: Kilépés")

tipusId="alma"
while tipusId=="alma" or tipusId not in range(len(tipusok)+1):
    try:
        tipusId=int(input("Válassz!"))
        if tipusId not in range(len(tipusok)+1):
            raise
    except:
        print("Válassz a listából!")


print("#"*35)
tipusId-=1
print("Típus:",tipusok[tipusId])
print("Mértékegységek:")

for i,elem in enumerate(egysegek[tipusId]):
    print("\t"+str(i+1)+":",elem)

print("\t0: Vissza")

egysegId1="alma"
while egysegId1=="alma" or egysegId1 not in range(len(egysegek[tipusId])+1):
    try:
        egysegId1=int(input("Válassz!"))
        if egysegId1 not in range(len(egysegek[tipusId])+1):
            raise
    except:
        print("Válassz a listából!")


for i,elem in enumerate(egysegek[tipusId]):
    print("\t"+str(i+1)+":",elem)

print("\t0: Vissza")

egysegId2="alma"
while egysegId2=="alma" or egysegId2 not in range(len(egysegek[tipusId])+1):
    try:
        egysegId2=int(input("Válassz!"))
        if egysegId2 not in range(len(egysegek[tipusId])+1):
            raise
    except:
        print("Válassz a listából!")

szam=float(input("Mennyiség: "))
egysegId1-=1
egysegId2-=1

if egysegId1<egysegId2:
    print(valtok[tipusId][egysegId1:egysegId2])
    szorzo=1
    for e in valtok[tipusId][egysegId1:egysegId2]:
        szorzo*=e

    
else:
    print(valtok[tipusId][egysegId2:egysegId1])
    for e in valtok[tipusId][egysegId2:egysegId1]):
        szorzo*=e
