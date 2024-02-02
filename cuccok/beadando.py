import random

szam = [random.randint(10000, 99999) for i in range(500)]
print(szam)
parosszamok= len([szamok for szamok in szam if szamok % 2 == 0])
print(parosszamok)

paratlanszamok= 0
for szamok in szam:
    if szamok % 2 != 0:
        paratlanszamok+= szamok
print("A kapott számok páratlan számainak összege:", paratlanszamok)

for szamok in szam:
    if 30000<szamok<39999:
        print(szamok)
