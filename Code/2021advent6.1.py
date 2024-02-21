file = open("2021Advent6.txt","r")
all = file.read()
all = all.split(",")
for i in range(len(all)):
    all[i]=int(all[i])


for n in range(80):
    for t in range(len(all)):
        if all[t] != 0:
            all[t]-=1
        else:
            all[t]=6
            all.append(8)
    

print(len(all))