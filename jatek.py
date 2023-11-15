def menu(lista):
    for i,elem in enumerate (lista):
        print("{}: {}".format(i+1,elem))

    valasztas=0
    while (valasztas<1 or valasztas>len(lista)) and valasztas!=69:
        try:
            valasztas=int(input("Válassz: "))
        except:
            pass

    return valasztas-1


lista=["előre", "hátra", "jobbra", "balra"]



#valasz=menu(lista)
#print(valasz,lista[valasz])
#import szoveghun as t
#Nyelv választás
nyelvLista=["Magyar", "English", "Deutsch", "Russian"]
nyelvId={"Magyar":"szoveghun","English":"szovegEng"}
print("Válassz nyelvet:")
while True:
    nyelvValasztas=menu(nyelvLista)
    print(nyelvLista[nyelvValasztas])
    if nyelvLista[nyelvValasztas] in nyelvId:
        break
    else:
        print("Sajnos ez a fordítás még nem készült el!")

if nyelvId[nyelvLista[nyelvValasztas]] =="szoveghun":
    import szoveghun as t
elif nyelvId[nyelvLista[nyelvValasztas]] =="szovegEng":
    import szovegEng as t
else:
    print(nyelvId[nyelvLista[nyelvValasztas]])


    
tortenet=[
        [
            1,#szál ID
            t.text["Reggel felébredtem. Mit tegyek?"],#szöveg
            [t.text["fogmosás"],t.text["reggeli"],t.text["öltözés"]],#választási lehetőségek
            [2,3,4] #Hova ugorjon
        ],
        [
            2,#szál ID
            t.text["Elmegyek fogatmosni. Sikálom rendesen, ahogy kell!"],#szöveg
            [t.text["fogmosás"],t.text["reggeli"],t.text["öltözés"]],#választási lehetőségek
            [2,3,4] #Hova ugorjon
        ],
        [
            3,#szál ID
            t.text["Kellene valamit enni! Anya csinált valamit? Nézzük meg!"],#szöveg
            [t.text["fogmosás"],t.text["reggeli"],t.text["öltözés"]],#választási lehetőségek
            [2,3,4] #Hova ugorjon
        ],
        [
            4,#szál ID
            t.text["Kissé hűvös van, Kelle valami ruha! \nFelveszek egy nadrágot, meg egy pólót!"],#szöveg
            [t.text["fogmosás"],t.text["reggeli"],t.text["öltözés"]],#választási lehetőségek
            [2,3,4] #Hova ugorjon
        ],
        [
            66, #szál ID
            "Vége mindennek...",#szoveg
            [],
            []
        ]
    ]

        
szalId=1

while True:
    temp=[]
    for e in tortenet:
        temp.append(e[0])
    #maskepp
    temp=[e[0] for e in tortenet]
    szalIndex=temp.index(szalId)

    print(tortenet[szalIndex][1])

    if tortenet[szalIndex][2] == []:
        break
    

    menuPont=menu(tortenet[szalIndex][2])

    if menuPont == 68:
        break
    szalId=tortenet[szalIndex][3][menuPont]

print("The End")
