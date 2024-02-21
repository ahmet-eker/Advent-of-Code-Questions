with open("2021Advent7.txt","r") as file:
    a = [int(i) for i in file.read().split(",")]

max_member = max(a)
min_member = min(a)


min_fuel=10000000000000000000

for t in range(min_member,max_member,1):
    sum_fuel=0
    for m in a:
        fuel=0
        for y in range(abs(m-t)):
            fuel+=y+1
        sum_fuel+=fuel
    min_fuel= min(min_fuel,sum_fuel)

print(min_fuel)