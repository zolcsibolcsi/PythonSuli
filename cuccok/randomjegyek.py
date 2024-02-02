import random


#12 fő, 8-12 jegy, jegy: 1-5

jegyek=[]
for i in range(12):
    egyDiak=[]
    for k in range(random.randrange(8,13)):
        jegy=random.randrange(1,6)
        egyDiak.append(jegy)
    jegyek.append(egyDiak)