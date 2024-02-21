import numpy as np

with open("2021Advent9.txt",'r') as input:
    a = input.read().split("\n")
    liste = []
    for t in a:
        geciciliste = []
        for i in t:
            geciciliste.append(i)
        liste.append(geciciliste)
    del geciciliste

en = len(liste[0])
boy = len(liste)


for a,t in enumerate(liste):
    for b,i in enumerate(t):
        liste[a][b]= int(i)


sum = 0

for a,t in enumerate(liste):
    for b,i in enumerate(t):
        
        if a == 0:
            if b == 0:
                if liste[a][b] < liste[a-1][b] and liste[a][b] < liste[a][b+1]:
                    sum += liste[a][b]+1
            elif b == en - 1:
                if liste[a][b] < liste[a+1][b] and liste[a][b] < liste[a][b-1]:
                    sum += liste[a][b]+1
            else:
                if liste[a][b] < liste[a+1][b] and liste[a][b] < liste[a][b+1] and liste[a][b] < liste[a][b-1]:
                    sum += liste[a][b]+1


        
        elif a == boy-1:
            if b == 0:
                if liste[a][b] < liste[a-1][b] and liste[a][b] < liste[a][b+1]:
                    sum += liste[a][b]+1
            elif b == en - 1:
                if liste[a][b] < liste[a-1][b] and liste[a][b] < liste[a][b-1]:
                    sum += liste[a][b]+1
            else:
                if liste[a][b] < liste[a-1][b] and liste[a][b] < liste[a][b+1] and liste[a][b] < liste[a][b-1]:
                    sum += liste[a][b]+1

        else:
            if b==0:
                if liste[a][b] < liste[a+1][b] and liste[a][b] < liste[a-1][b] and liste[a][b] < liste[a][b+1]:
                    sum += liste[a][b]+1
            elif b == en - 1:
                if liste[a][b] < liste[a+1][b] and liste[a][b] < liste[a-1][b] and liste[a][b] < liste[a][b-1]:
                    sum += liste[a][b]+1
            else:
                if liste[a][b] < liste[a+1][b] and liste[a][b] < liste[a-1][b] and liste[a][b] < liste[a][b-1] and liste[a][b] < liste[a][b+1]:
                    sum += liste[a][b]+1

print(sum)