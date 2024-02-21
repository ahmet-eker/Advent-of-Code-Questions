i=0
with open("2021Advent8.txt","r") as input:
    for t in [t.split(" | ")[1] for t in [i for i in input.read().split("\n")]]:
        for c in [g for g in t.split(" ")]:
            if len(c)==2 or len(c)==3 or len(c)==4 or len(c)==7:i+=1

print(i)

    
    