with open("2019Advent2.txt","r") as file:
    k = [int(i) for i in file.read().split(",")]

def func(k):

    a = k.copy()

    for x in range(0,len(a),4):
        operator = a[x]
        number1=a[a[x+1]]
        number2=a[a[x+2]]
        if operator==99:
            return a[0]        
        elif operator==1:
            a[a[x+3]]=number1+number2
        elif operator==2:
            a[a[x+3]]=number1*number2

    return a[0]

for y in range(100):
    for u in range(100):
        k[1]=y
        k[2]=u
        if func(k) == 19690720:
            print(y,u,sep="")
        