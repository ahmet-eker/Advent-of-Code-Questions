file = open("2021Advent1.txt",'r')
liste = []
for i in file.readlines():
    liste.append(int(i))
a = liste
print(len(a))
k = l = m = 0
for x in range(len(a)-3):
    if a[x]+a[x+1]+a[x+2]<a[x+1]+a[x+2]+a[x+3]:
        k+=1
    elif a[x]+a[x+1]+a[x+2]==a[x+1]+a[x+2]+a[x+3]:
        l+=1
    else:
        m+=1
print(k)
print(l)
print(m)




"""
import numpy as np
with open('Depth.txt', 'r') as f:
    lines = f.readlines()
    measurements = [int(entry.strip()) for entry in lines]
sliding_windows = np.convolve(measurements, np.ones(3), 'valid')
prev_entry = sliding_windows[0]
increases = 0
for entry in sliding_windows[1:]:
    if entry > prev_entry:
        increases += 1
    prev_entry = entry

print(increases)
"""