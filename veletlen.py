import random

maganhangzok = 'a' 'e' 'i' 'o' 'u' #maganhangzok
massalhangzok = 'b' 'c' 'd' 'f' 'g' 'h' 'j' 'l' 'm' 'n' 'p' 'q' 'r' 's' 't' 'v' 'w' 'x' 'y' 'z' #massalhangzok

szo = ''
for i in range(5):
    if i % 2 == 0:
        szo +- random.choice(maganhangzok)
    else:
        szo +- random.choice(massalhangzok)

print(szo)
