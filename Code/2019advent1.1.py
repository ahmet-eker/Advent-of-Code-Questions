with open("2019Advent1.txt","r") as file:
    a = [int(i) for i in file.read().split("\n")]

sum = 0
for t in a:
    b = int(t/3)-2
    sum+=b
print(sum)

