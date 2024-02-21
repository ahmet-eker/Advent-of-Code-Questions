with open("2021Advent6.txt","r") as file:
    a = [int(i) for i in file.read().split(",")]

number_list = [0] * 9

for t in a:
    number_list[t]+=1


new_list = number_list.copy()


for t in range(256):
    for c in range(len(number_list)):
        if c == 6:
            number_list[c]=new_list[c+1]+new_list[0]
        elif c == 8:
            number_list[c]=new_list[0]
        else:
            number_list[c]=new_list[c+1]
    new_list = number_list.copy()


print(sum(number_list))


"""
for m in range(256):
    a1 = number_list[0]
    a2 = number_list[1]
    a3 = number_list[2]
    a4 = number_list[3]
    a5 = number_list[4]
    a6 = number_list[5]
    a7 = number_list[6]
    a8 = number_list[7]
    a9 = number_list[8]

    number_list[0] = a2
    number_list[1] = a3
    number_list[2] = a4
    number_list[3] = a5
    number_list[4] = a6
    number_list[5] = a7
    number_list[6] = a8 + a1
    number_list[7] = a9
    number_list[8] = a1

print(sum(number_list))
"""