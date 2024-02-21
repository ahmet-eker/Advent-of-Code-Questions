from numpy import minimum

with open("2021Advent7.txt","r") as file:
    a = [int(i) for i in file.read().split(",")]

max = max(a)
min = min(a)

k = 100000000000000000
for t in range(min,max,1):
    l=0
    for m in a:
        l+=abs(m-t)
    k = minimum(k,l)


for h in range(min,max,1):
    l=0
    for g in a:
       l+=abs(g-h)
    if l==k:
        print(h)
        break

print(k)