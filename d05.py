import math

rowMax = 128
colMax = 7
lower = {"F", "L"}
upper = {"B", "R"}

file = open("input/d05.txt", 'r')

def getLocation (max, directions):
    bounds = [0, max]
    for d in directions:
        newBounds = (bounds[0] + bounds[1]) / 2
        if d in lower:
            bounds[1] = math.floor(newBounds)
        elif d in upper:
            bounds[0] = math.ceil(newBounds)
    return bounds[0]

def findMissing (ids):
    ids.sort()
    offset = ids[0]
    bounds = [0, len(ids) - 1]
    while bounds[0] + 1 != bounds[1]:
        mid = math.floor((bounds[0] + bounds[1]) / 2)
        if ids[mid] != offset + mid:
            bounds[1] = mid
        else:
            bounds[0] = mid
    return ids[bounds[0]] + 1

ids = []
maxId = 0
for line in file:
    line = line.rstrip()
    rowDir = line[0:7]
    row = getLocation(rowMax, rowDir)
    colDir = line[7:]
    col = getLocation(colMax, colDir)
    id = (row * 8) + col
    ids.append(id)
    maxId = max(maxId, id)

print(maxId)
print(findMissing(ids))