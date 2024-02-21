with open("2019Advent3.txt","r") as input:
    wire1 = input.readline().strip().split(",")
    wire2 = input.readline().strip().split(",")

coordinate1 = [0,0]
wire1_locations = []
for command in wire1:
    operator = command[0]
    liste = command[1:]
    number = ""
    for t in liste:
        number += t

    number=int(number)

    if operator == "R":
        for h in range(number):
            coordinate1[0]+=1
            a = coordinate1.copy()
            wire1_locations.append(a)

    elif operator == "L":
        for h in range(number):
            coordinate1[0]-=1
            a = coordinate1.copy()
            wire1_locations.append(a)

    elif operator == "U":
        for h in range(number):
            coordinate1[1]+=1
            a = coordinate1.copy()
            wire1_locations.append(a)

    elif operator == "D":
        for h in range(number):
            coordinate1[1]-=1        
            a = coordinate1.copy()
            wire1_locations.append(a)
            






coordinate2 = [0,0]
wire2_locations = []
for command in wire2:
    operator = command[0]
    liste = command[1:]
    number = ""
    for t in liste:
        number += t

    number=int(number)

    if operator == "R":
        for h in range(number):
            coordinate2[0]+=1
            a = coordinate2.copy()
            wire2_locations.append(a)

    elif operator == "L":
        for h in range(number):
            coordinate2[0]-=1
            a = coordinate2.copy()
            wire2_locations.append(a)

    elif operator == "U":
        for h in range(number):
            coordinate2[1]+=1
            a = coordinate2.copy()
            wire2_locations.append(a)

    elif operator == "D":
        for h in range(number):
            coordinate2[1]-=1        
            a = coordinate2.copy()
            wire2_locations.append(a)




liste= []

for t in wire1_locations:
    if t in wire2_locations:
        a = t
        liste.append(a)


k=[]
for i in liste:
    p = int(wire1_locations.index(i))+1
    l = int(wire2_locations.index(i))+1
    k.append(p+l)

print(min(k))