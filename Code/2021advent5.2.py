file =open("2021Advent5.txt","r")

firstlist = []

for star_finish_dot in file.readlines():
    a = star_finish_dot.split(" -> ")
    for t in a:
        h = t.split(",")
        firstlist.append(h[0])
        firstlist.append(h[1])

secondlist =[]
for t in range(int(len(firstlist)/4)):
    nothing=[]
    nothing.append(firstlist[4*t])
    nothing.append(firstlist[(4*t)+1])
    nothing.append(firstlist[(4*t)+2])
    nothing.append(firstlist[(4*t)+3])
    secondlist.append(nothing)
    
for o in range(len(secondlist)):
    for t in range(len(secondlist[o])):
        secondlist[o][t]=int(secondlist[o][t])

thirdlist=[]

for y in secondlist:
    if y[0]==y[2] or y[1]==y[3] or abs(y[0]-y[2])==abs(y[1]-y[3]):
        thirdlist.append(y)

coordinates = []

for u in thirdlist:
    if u[0]==u[2]:
        for s in range(abs(u[1]-u[3])+1):
            member = []
            member.append(u[0])
            member.append(min(u[1],u[3])+s)
            coordinates.append(member)
        
    elif u[1]==u[3]:
        for l in range(abs(u[0]-u[2])+1):
            member = []
            member.append(min(u[0],u[2])+l)
            member.append(u[1])
            coordinates.append(member)
    
    else:
        for h in range(abs(u[0]-u[2])+1):
            if u[0]>u[2]:
                member = []
                member.append(u[0]-h)
            else:
                member = []
                member.append(u[0]+h)

            if u[1]>u[3]:
                member.append(u[1]-h)
                coordinates.append(member)
            else:
                member.append(u[1]+h)
                coordinates.append(member)
    
maxlist=[]

for j in coordinates:
    maxnumber = coordinates.count(j)
    if maxnumber >=2 and j not in maxlist:
        maxlist.append(j)

print(len(maxlist))

