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
    newPos = []
    for i in range(2):
        newPos.append(currPos[i] + (dirs[dir][i] * steps))
    return newPos

def partOne ():
    currDir = 0
    pos = [0, 0]

    for line in file:
        line = line.rstrip()
        i = line[:1]
        v = int(line[1:])
        print(i, v)
        if i == "R":
            currDir = (currDir + v) % 360
        elif i == "L":
            currDir = (currDir - v) % 360
        elif i == "F":
            pos = move(pos, rDirs[currDir], v)
        else:
            pos = move(pos, i, v)
    print(pos, (abs(pos[0]) + abs(pos[1])))

partOne()