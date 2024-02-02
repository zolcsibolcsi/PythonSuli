def maxKeres(lista):
    legnagyobb=lista[0]
    maxIndex = 0
    for i in range(len(lista)):
        if lista[i]>legnagyobb:
            legnagyobb=lista[i]
            maxIndex=i
    return (legnagyobb,maxIndex)



lista=[100,35,69,73,42,73,55,66,33,22,70,81]
legnagyobb,maxIndex=maxKeres(lista)

print(maxIndex,legnagyobb)
