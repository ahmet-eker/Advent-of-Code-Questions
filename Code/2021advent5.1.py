file =open("2021Advent5.txt","r")
linelist=[]
newlist=[]
for line in file.readlines():
    a = line.split(" -> ")
    for m in range(len(a)):
        b=a[m].split(",")
        linelist.append(b)

for p in range(0,len(linelist),2):
    if int(linelist[p][0]) == int(linelist[p+1][0]):
        member = linelist[p] + linelist[p+1]
        newlist.append(member)

    elif int(linelist[p][1])==int(linelist[p+1][1]):
        member = linelist[p] + linelist[p+1]
        newlist.append(member)

    elif int(linelist[p][0])-int(linelist[p][1])==int(linelist[p+1][0])-int(linelist[p+1][1]):
        member = linelist[p] + linelist[p+1]
        newlist.append(member)


coordinates=[]

for y in range(len(newlist)):
    if int(newlist[y][0])==int(newlist[y][2]):
        for m in range(abs(int(newlist[y][1])-int(newlist[y][3]))+1):
            member2=[]
            member2.append(newlist[y][0])
            member2.append(str(min(int(newlist[y][1]),int(newlist[y][3]))+m))
            coordinates.append(member2)
    elif int(newlist[y][1])==int(newlist[y][3]):
        for k in range(abs(int(newlist[y][0])-int(newlist[y][2]))+1):
            member2 = []
            member2.append(str(min(int(newlist[y][0]),int(newlist[y][2]))+k))
            member2.append(newlist[y][1])
            coordinates.append(member2)
    else:
        member2 = []
        for r in range(abs(int(newlist[y][0])-int(newlist[y][1]))+1):
            if newlist[y][0]>newlist[y][2]:
                member2.append(str(int(newlist[y][0])-r))
            else:
                member2.append(str(int(newlist[y][0])+r))

            if newlist[y][1]>newlist[y][3]:
                member2.append(str(int(newlist[y][1])-r))
            else:
                member2.append(str(int(newlist[y][1])+r))
            coordinates.append(member2)


maxlist=[]

for t in range(len(coordinates)):
    j = coordinates.count(coordinates[t])
    maxlist.append(int(j))


prolist=[]

for o in range(len(maxlist)):
    if maxlist[o]>=2:
        if coordinates[o] not in prolist:
            prolist.append(coordinates[o])


u = len(prolist)

print(u)