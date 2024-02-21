file = open("2021Advent3.txt",'r')
read_file = file.read()
splitted_list = read_file.split("\n")


most_liste = []

for x in range(len(splitted_list[0])):
    k=l=0
    for member_binary in splitted_list:
        t = member_binary[x]
        
        if t=='1':
            k+=1
        else:
            l+=1

    if k>l:
        most_liste.append(1)
    else:
        most_liste.append(0)

print(most_liste)


least_liste = []

for x in range(len(splitted_list[0])):
    k=l=0
    for member_binary in splitted_list:
        t = member_binary[x]
        
        if t=='0':
            k+=1
        else:
            l+=1

    if k>l:
        least_liste.append(1)
    else:
        least_liste.append(0)

print(least_liste)



def binary_to_integer(y):
    sum=0
    for z in range(len(y)):
        if y[len(y)-1-z]==1:
            sum += pow(2,z)
    return sum
print(most_liste)
h1 = binary_to_integer(most_liste)
h2 = binary_to_integer(least_liste)
print(h1)
print(h2)
print(h1*h2)
