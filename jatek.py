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
            [t.text["koncert"]],#választási lehetőségek
            [5], #Hova ugorjon
        ],
        [
            5,#szál ID
            t.text["Ma koncertre megyek, elötte dönteni kéne, hogy itthon vagy egy étteremben eszek."],#szöveg
            [t.text["otthon"],t.text["étteremben"]],#választási lehetőségek
            [6,7], #Hova ugorjon
        ],
        [
            6,#szál ID
            t.text["Itthon ettem, most elindulok a koncertre, jegyet az odaúton vagy a helyszínen vegyek?"],#szöveg
            [t.text["odaúton"],t.text["helyszínen"]],#választási lehetőségek
            [9,8], #Hova ugorjon
        ],
        [
            7,#szál ID
            t.text["Étteremben ettem, most elinduok a koncertre, jegyet az odaúton vagy a helyszínen vegyek?"],#szöveg
            [t.text["odaúton"],t.text["helyszínen"]],#választási lehetőségek
            [9,8], #Hova ugorjon
        ],
        [
            8,#szál ID
                t.text["helyszínen veszem a jegyet, beállok a sorba."],#szöveg
                [t.text["kártyával fizetek"],t.text["készpénzel fizetek"]],#választási lehetőségek
                [10,10], #Hova ugorjon
        ],
        [
            9,#szál ID
                t.text["ideúton vettem a jegyet, nem kell sorban állnom."],#szöveg
                [t.text["iszok valamit"],t.text["megpróbálok minél közelebb jutni a színpadhoz"]],#választási lehetőségek
                [11,15], #Hova ugorjon
        ],
        [
            10,#szál ID
                t.text["Fizettem, mit tegyek?"],#szöveg
                [t.text["iszok valamit"],t.text["megpróbálok minél közelebb jutni a színpadhoz"]],#választási lehetőségek
                [11], #Hova ugorjon
        ],
        [
            11,#szál ID
                t.text["Mit igyak?"],#szöveg
                [t.text["vodka alma"],t.text["jager"],t.text["Cappy"]],#választási lehetőségek
                [12], #Hova ugorjon
        ],
         [
            12,#szál ID
                t.text["Koncert után hova menjek?"],#szöveg
                [t.text["Haza"],t.text["Mekibe"]],#választási lehetőségek
                [13,14], #Hova ugorjon
        ],
        [
            13,#szál ID
                t.text["Haza megyek, majd lefekszek aludni"],#szöveg
                [t.text["Vége"]],#választási lehetőségek
                [69], #Hova ugorjon
        ],
        [
            14,#szál ID
                t.text["Elmegyek Mekibe majd utánna haza."],#szöveg
                [t.text["Vége"]],#választási lehetőségek
                [66], #Hova ugorjon
        ],
        [
            15,#szál ID
                t.text["Sikerült ideérnem időben ezert második sorban állok"],#szöveg
                [t.text["Vége a koncertnek"]],#választási lehetőségek
                [12], #Hova ugorjon
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
