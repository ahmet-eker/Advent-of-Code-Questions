with open("2019Advent4.txt","r") as input:
    a = input.read().split("-")

def func(integer):
    for m in list(str(integer)):
        if str(integer).count(m) >= 2:
            return True

    return False

i=0
for t in range(int(a[0]),int(a[1])):
    if list(str(t))==sorted(list(str(t))) and func(t): 
        i+=1

print(i)