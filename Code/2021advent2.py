file = open("2021Advent2.txt",'r')
lines = file.readlines()
aim = 0
horizontalposition = 0
depth =0
for i in range(len(lines)):
    seperate = lines[i].split(" ")
    if seperate[0]=="up":
        aim -= int(seperate[1])
    elif seperate[0]=="down":
        aim += int(seperate[1])
    else:
        horizontalposition += int(seperate[1])
        depth += aim*int(seperate[1])

print(depth*horizontalposition)
