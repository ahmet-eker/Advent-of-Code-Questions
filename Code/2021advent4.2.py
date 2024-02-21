file = open("2021Advent4.txt",'r')
f = file.readline()
f2 = file.readline()

girdiler = f.split(",")
girdiler2 = f2.split(",")
girdiler3 = girdiler + girdiler2

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



my_erase_list=[]


for h in range(len(girdiler3)):
    
    k = int(girdiler3[h])
    for s in range(len(listofall)):
        for g in range(len(listofall[s])):            
            try:    
                if k == int(listofall[s][g]):
                    listofall[s][g] = listofall[s][g]+"*"
            except:
                continue


    for g in range(len(listofall)):
        j = "*"

        if (j in (listofall[g][0])) and (j in (listofall[g][1])) and (j in (listofall[g][2])) and (j in (listofall[g][3])) and (j in (listofall[g][4])):
            if listofall[g] not in my_erase_list:
                my_erase_list.append(listofall[g])

        elif (j in (listofall[g][5])) and (j in (listofall[g][6])) and (j in (listofall[g][7])) and (j in (listofall[g][8])) and (j in (listofall[g][9])):
            if listofall[g] not in my_erase_list:
                my_erase_list.append(listofall[g])
                
        elif (j in (listofall[g][10])) and (j in (listofall[g][11])) and (j in (listofall[g][12])) and (j in (listofall[g][13])) and (j in (listofall[g][14])):
            if listofall[g] not in my_erase_list:
                my_erase_list.append(listofall[g])

        elif (j in (listofall[g][15])) and (j in (listofall[g][16])) and (j in (listofall[g][17])) and (j in (listofall[g][18])) and (j in (listofall[g][19])):
            if listofall[g] not in my_erase_list:
                my_erase_list.append(listofall[g])
                
        elif (j in (listofall[g][20])) and (j in (listofall[g][21])) and (j in (listofall[g][22])) and (j in (listofall[g][23])) and (j in (listofall[g][24])):
            if listofall[g] not in my_erase_list:
                my_erase_list.append(listofall[g])

        elif (j in (listofall[g][0])) and (j in (listofall[g][5])) and (j in (listofall[g][10])) and (j in (listofall[g][15])) and (j in (listofall[g][20])):
            if listofall[g] not in my_erase_list:
                my_erase_list.append(listofall[g])

        elif (j in (listofall[g][1])) and (j in (listofall[g][6])) and (j in (listofall[g][11])) and (j in (listofall[g][16])) and (j in (listofall[g][21])):
            if listofall[g] not in my_erase_list:
                my_erase_list.append(listofall[g])

        elif (j in (listofall[g][2])) and (j in (listofall[g][7])) and (j in (listofall[g][12])) and (j in (listofall[g][17])) and (j in (listofall[g][22])):
            if listofall[g] not in my_erase_list:
                my_erase_list.append(listofall[g])

        elif (j in (listofall[g][3])) and (j in (listofall[g][8])) and (j in (listofall[g][13])) and (j in (listofall[g][18])) and (j in (listofall[g][23])):
            if listofall[g] not in my_erase_list:
                my_erase_list.append(listofall[g])

        elif (j in (listofall[g][4])) and (j in (listofall[g][9])) and (j in (listofall[g][14])) and (j in (listofall[g][19])) and (j in (listofall[g][24])):
            if listofall[g] not in my_erase_list:
                my_erase_list.append(listofall[g])
    
    if len(my_erase_list)==len(listofall):
        lastmember=int(girdiler3[h])
        break



sum = 0
for u in range(len(my_erase_list[-1])):
    if "*"  not in my_erase_list[-1][u]:
        sum+=int(my_erase_list[-1][u])
print(sum)
print(lastmember)
    
print(sum*lastmember)