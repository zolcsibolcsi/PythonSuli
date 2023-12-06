f=open("bela.txt","w")

#f.write("1")
for i in range(100):
    f.writelines(str(i)+"\n")

f.close()

open("bela2.txt","w").write("\n".join([str(i) for i in range(100)]))


f=open("bela.txt","r")
lista=[]
for egySor in f:
    lista.append(egySor.strip())
f.close()
print(lista)

f=open("bela.txt","r")
lista=[egySor.strip() for egySor in f.readlines()]
f.close()
print(lista)