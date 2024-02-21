with open("2019Advent1.txt","r") as file:
    a = [int(i) for i in file.read().split("\n")]

def func(value):
    sum=0
    while value>=0:
        value=int(value/3)-2
        if value>0:
            sum+=value

    return sum


bigsum=0
for t in a:
    bigsum+=func(t)

print(bigsum)




sum = 0
for t in a:
    b = int(t/3)-2
    sum+=b
print(sum)
