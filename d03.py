file = open("input/d03.txt", 'r')

lines = [line.rstrip() for line in file]

i = 0
j = 0
trees = 0

while j < len(lines):
    if lines[j][i] == '#':
        trees += 1
    
    i = (i + 3) % len(lines[j])
    j += 1

print(trees)