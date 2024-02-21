file = open("2021Advent4.txt",'r')
f = file.readline()
f2 = file.readline()

girdiler = f.split(",")
girdiler2 = f2.split(",")
girdiler3 = girdiler + girdiler2
print(girdiler3)

#print(girdiler)

listofall=[]

for line in file.readlines():
    a = line.split(" ")
    erase_list=[]
    for t in range(len(a)):
        if a[t]=="" or a[t]=="\n":
            erase_list.append(a[t])
        
    for k in range(len(erase_list)):
        a.remove(erase_list[k])
    if a!=[]:
        listofall.append(a)
#print(listofall)
listtest=listofall.copy()
listofall.clear()

for x in range(int(len(listtest)/5)):
    x*=5
    listofall.insert(int(x/5),listtest[x]+listtest[x+1]+listtest[x+2]+listtest[x+3]+listtest[x+4])
#print(listofall)

h=0
while h < len(girdiler3):

    k = int(girdiler3[h])
    for s in range(len(listofall)):
        for g in range(len(listofall[s])):            
            try:    
                if k == int(listofall[s][g]):
                    listofall[s][g] = listofall[s][g]+"*"
            except:
                continue
    #print(listofall)
    #print("\n \n")
    e =0
    while e <len(listofall):
        j="*"

        if (j in (listofall[e][0])) and (j in (listofall[e][1])) and (j in (listofall[e][2])) and (j in (listofall[e][3])) and (j in (listofall[e][4])):
            print("That's it you won number", e)
            print(listofall)
            e+=100000000
            h+=100000000

        elif (j in (listofall[e][5])) and (j in (listofall[e][6])) and (j in (listofall[e][7])) and (j in (listofall[e][8])) and (j in (listofall[e][9])):
            print("That's it you won number", e)
            print(listofall)
            e+=100000000
            h+=100000000
                
        elif (j in (listofall[e][10])) and (j in (listofall[e][11])) and (j in (listofall[e][12])) and (j in (listofall[e][13])) and (j in (listofall[e][14])):
            print("That's it you won number", e)
            print(listofall)
            e+=100000000
            h+=100000000

        elif (j in (listofall[e][15])) and (j in (listofall[e][16])) and (j in (listofall[e][17])) and (j in (listofall[e][18])) and (j in (listofall[e][19])):
            print("That's it you won number", e)
            print(listofall)
            e+=100000000
            h+=100000000
            
        elif (j in (listofall[e][20])) and (j in (listofall[e][21])) and (j in (listofall[e][22])) and (j in (listofall[e][23])) and (j in (listofall[e][24])):
            print("That's it you won number", e)
            print(listofall)
            e+=100000000
            h+=100000000

        elif (j in (listofall[e][0])) and (j in (listofall[e][5])) and (j in (listofall[e][10])) and (j in (listofall[e][15])) and (j in (listofall[e][20])):
            print("That's it you won number", e)
            print(listofall)
            e+=100000000
            h+=100000000

        elif (j in (listofall[e][1])) and (j in (listofall[e][6])) and (j in (listofall[e][11])) and (j in (listofall[e][16])) and (j in (listofall[e][21])):
            print("That's it you won number", e)
            print(listofall)
            e+=100000000
            h+=100000000

        elif (j in (listofall[e][2])) and (j in (listofall[e][7])) and (j in (listofall[e][12])) and (j in (listofall[e][17])) and (j in (listofall[e][22])):
            print("That's it you won number", e)
            print(listofall)
            e+=100000000
            h+=100000000

        elif (j in (listofall[e][3])) and (j in (listofall[e][8])) and (j in (listofall[e][13])) and (j in (listofall[e][18])) and (j in (listofall[e][23])):
            print("That's it you won number", e)
            print(listofall)
            e+=100000000
            h+=100000000

        elif (j in (listofall[e][4])) and (j in (listofall[e][9])) and (j in (listofall[e][14])) and (j in (listofall[e][19])) and (j in (listofall[e][24])):
            print("That's it you won number", e)
            print(listofall)
            e+=100000000
            h+=100000000
        
        e+=1
    h+=1

h-=100000001
e-=100000001

tableno=e
lastmember=girdiler3[h]


sum = 0

for u in range(len(listofall[e])):
    if "*" in listofall[e][u]:
        continue
    else:
        sum += int(listofall[e][u])
print(sum)
print(lastmember)
answer=sum*int(lastmember)
print(answer)
print(listofall[e])