import random
bekert = ""
while bekert != 0:
    valaszto=["Ötöslottó","Hatoslottó","Skandinávlottó","Totó"]
    for i,elem in enumerate(valaszto):
        print(i+1,".",elem)
    print("0 : Kilépés")
    print("#"*40)
    bekert = int(input("Adj meg egy számot a fentiek közül:"))
    print("#"*40)
    if bekert == 1:
        
        #otoslotto
        otosLista=[]

        while len(otosLista)<= 4:
            randomSzam = random.randint(1,90)
            if randomSzam not in otosLista:
                otosLista.append(randomSzam)

        print ("A gép által sorsolt Ötöslottó számok:",otosLista)
        print("#"*40)
    elif bekert == 2:
    

        #hatoslotto
        hatosLista=[]

        while len(hatosLista)<= 5:
            randomSzam = random.randint(1,45)
            if randomSzam not in hatosLista:
                hatosLista.append(randomSzam)

        print ("A gép által sorsolt Hatoslottó számok:",hatosLista)
        print("#"*40)
    elif bekert == 3:
    
        #skandinavlotto

        skandinavLista=[]

        while len(skandinavLista)<= 6:
            randomSzam = random.randint(1,35)
            if randomSzam not in skandinavLista:
                skandinavLista.append(randomSzam)

        print ("A gép által sorsolt Skandináv lottó számok:",skandinavLista)
        print("#"*40)
    elif bekert == 4:
    

#toto
toto=["1","2","x"]
toto2=[]

while len(toto2)<= 13:
    index = random.randint(0,2)
    toto2.append(toto[index])

print (toto2)
elif bekert == 0:
    break
