file = open("2021Advent3.txt",'r')
read_file = file.read()
splitted_list = read_file.split("\n")

splitted_list2 = splitted_list[:]


for f in range(len(splitted_list[0])):
    if len(splitted_list)!=1:
        k=l=0
        for o in range(len(splitted_list)):
            if splitted_list[o][f]=='1':
                k+=1
            else:
                l+=1

        clear_list=[]

        if k>=l:       #1 daha fazla
            for x in range(len(splitted_list)):
                if splitted_list[x][f]=='0':
                    clear_list.append(splitted_list[x])
            for m in clear_list:
                splitted_list.remove(m)
            
        else:
            for x in range(len(splitted_list)):
                if splitted_list[x][f]=='1':
                    clear_list.append(splitted_list[x])
            for m in clear_list:
                splitted_list.remove(m)



a1 = splitted_list[0]



for f in range(len(splitted_list2[0])):
    if len(splitted_list2)!=1:
        k=l=0
        for o in range(len(splitted_list2)):
            if splitted_list2[o][f]=='1':
                k+=1
            else:
                l+=1

        clear_list2=[]

        if k<l:       #1 daha fazla
            for x in range(len(splitted_list2)):
                if splitted_list2[x][f]=='0':
                    clear_list2.append(splitted_list2[x])
            for m in clear_list2:
                splitted_list2.remove(m)
            
        else:
            for x in range(len(splitted_list2)):
                if splitted_list2[x][f]=='1':
                    clear_list2.append(splitted_list2[x])
            for m in clear_list2:
                splitted_list2.remove(m)


a2 = splitted_list2[0]


def binary_to_integer(y):
    sum = 0
    for t in range(len(y)):
        if y[len(y)-1-t]=='1':
            sum+=pow(2,t)
    return sum

p1=binary_to_integer(a1)
p2=binary_to_integer(a2)

print(p1*p2)
