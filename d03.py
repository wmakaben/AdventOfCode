import math
file = open("input/d03.txt", 'r')

lines = [line.rstrip() for line in file]

# i = 0
# j = 0
# trees = 0

# while j < len(lines):
#     if lines[j][i] == '#':
#         trees += 1
    
#     i = (i + 3) % len(lines[j])
#     j += 1

# print(trees)

slopes = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]
]

totals = []

for slope in slopes:
    i = 0
    j = 0
    trees = 0
    while j < len(lines):
        if lines[j][i] == '#':
            trees += 1
        i = (i + slope[0]) % len(lines[j])
        j += slope[1]
    totals.append(trees)

print(math.prod(totals))
