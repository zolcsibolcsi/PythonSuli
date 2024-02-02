#irassatok ki az elso 50 nem negativ szamot!

for i in range(0,51):
    print(i)

#irassatok ki a kétjegyű számokat!

for y in range(10,100):
    print(y)

#irassatok ki 100-nal kisebb 7-tel oszthato szamokat!

for x in range(1,101,7):
    print(x)
    
#irassatok ki 500 es 2000 kozott azokat a szamokat, ahol a tizesek helyen 8 van!

for szam in range(500, 2001):
    tizesek_helye = szam // 10 % 10  
    if tizesek_helye == 8:
        print(szam)



#Szamold meg mennyi haromjegyu negyzetszam van
               
for n in range(10, 32):
    negyzet = n ** 2
    if 100 <= negyzet <= 999:
        print(negyzet)
#rajzoljunk egy karacsonyfat karakterekbol lehetoleg ciklussal


num = 3
for i in range(1, num+1):
	print(" "*(2*num-i+3), end="")
	for j in range(1, i+1):
		print("*", end=" ")
	print()

for i in range(1, num+3):
	print(" "*(2*num-i+1), end="")
	for j in range(-1, i+1):
		print("*", end=" ")
	print()

for i in range(1, num+5):
	print(" "*(2*num-i), end="")
	for j in range(-2, i+1):
		print("*", end=" ")
	print()

for i in range(1, num+3):
	print(" "*((2*num)), end="")
	print("* "*3)



num=3
for i in range(1, num+1):
    print(" "*(num-i+3), end="")
    for j in range(1, i+1):
            print("*", end=" ")
    print()

#bekeres 
