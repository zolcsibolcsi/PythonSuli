

lista=[]

beker="menjé' be"

while beker!="":
    beker=input("Adj meg valamit: ")
    if beker != "":
        lista.append(beker)

print(lista)
utolso=lista[-3:]
utolso.sort()

lista.sort()

for e in lista:
    print(e)

for e in lista[-3:]:
    print(e)
    
for e in utolso:
    print(e)
