adatok=[]

f=open("fob2016.txt")
for sor in f:
    adatok.append(sor.strip("\n").split(";"))
f.close()

for i in adatok:
    print(i)