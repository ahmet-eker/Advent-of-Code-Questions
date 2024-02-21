with open("2021Advent8.txt","r") as input:
    #input = [k.split(" | ")[1] for k in [i for i in input.read().split("\n")]]
    input = [i.strip() for i in input.readline().split(" | ")[1].split(" ")]

print(input)
mydict = {1: [3,6], 2:[1,3,4,5,7], 3:[1,3,4,6,7], 4:[2,3,4,6], 5:[1,2,4,6,7], 6:[1,2,4,5,6,7], 7:[1,3,6]}

k = []
for t in input:
    k.append(len(t))

print(k)


"""
 11111 
2     3
2     3
 44444
5     6
5     6
 77777

"""