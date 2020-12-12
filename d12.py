file = open("input/d12.txt", 'r')

dirs = {
    "E": [1, 0],
    "S": [0, -1],
    "W": [-1, 0],
    "N": [0, 1]
}

rDirs = {
    0: "E",
    90: "S",
    180: "W",
    270: "N"
}

def move (currPos, dir, steps):
    return [cp + (d * steps) for cp, d in zip(currPos, dirs[dir])]

def partOne ():
    currDir = 0
    pos = [0, 0]

    for line in file:
        line = line.rstrip()
        i = line[:1]
        v = int(line[1:])
        if i == "R":
            currDir = (currDir + v) % 360
        elif i == "L":
            currDir = (currDir - v) % 360
        elif i == "F":
            pos = move(pos, rDirs[currDir], v)
        else:
            pos = move(pos, i, v)
    print(pos, (abs(pos[0]) + abs(pos[1])))

def swapAndNegate (pos, idx):
    newPos = list(reversed(pos))
    newPos[idx] = newPos[idx] * -1
    return newPos

# Only accepts degrees of 90, 180, 270
def rotate (pos, dir, deg):
    if deg == 180:
        return [p * -1 for p in pos]
    elif (dir == "L" and deg == 90) or (dir == "R" and deg == 270):
        return swapAndNegate(pos, 0)
    elif (dir == "R" and deg == 90) or (dir == "L" and deg == 270):
        return swapAndNegate(pos, 1)

def partTwo ():
    sPos = [0, 0]
    wDist = [10, 1]
    for line in file:
        line = line.rstrip()
        i = line[:1]
        v = int(line[1:])
        if i == "R" or i == "L":
            wDist = rotate(wDist, i, v)
        elif i == "F":
            sPos = [s + (v * w) for s, w in zip(sPos, wDist)]
        else:
            wDist = move(wDist, i, v)
        # print(i, v, "\t", sPos, wDist)
    print(sPos, (abs(sPos[0]) + abs(sPos[1])))

# partOne()
partTwo()