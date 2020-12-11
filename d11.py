from copy import deepcopy

file = open("input/d11.txt", 'r')
lines = [list(line.rstrip().replace("L", "#")) for line in file]
# lines = [list(line.rstrip()) for line in file]


def printLayout (seats):
    for line in seats:
        print("".join(line))

def padLayout (seats):
    for row in seats:
        row.insert(0, '.')
        row.append('.')
    seats.insert(0, ['.'] * len(seats[0]))
    seats.append(['.'] * len(seats[0]))

# Assumes 1 < i/j < len(row/col) - 1
def getAdjacentCount (seats, i, j):
    count = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if seats[x][y] == '#':
                count += 1
    if seats[i][j] == '#':
        count -= 1
    return count

def getOccupied(seats):
    occupied = 0
    for row in seats:
        occupied += row.count('#')
    print(occupied)

def partOne (seatLayout):
    layout = deepcopy(seatLayout)
    padLayout(layout)

    while True:
        changed = False
        newLayout = deepcopy(layout)
        for i in range(1, len(layout) - 1):
            for j in range(1, len(layout[i]) - 1):
                if layout[i][j] == '.':
                    continue
                adjacent = getAdjacentCount(layout, i, j)
                if adjacent == 0 and newLayout[i][j] != '#':
                    newLayout[i][j] = '#'
                    changed = True
                elif adjacent > 3 and newLayout[i][j] != 'L':
                    newLayout[i][j] = 'L'
                    changed = True
        if changed == False:
            break
        layout = newLayout

    getOccupied(layout)

# This is terrible but it'll do
def getVisible (seats, i, j):
    count = 0
    dirs = range(-1, 2)
    for xStep in dirs:
        for yStep in dirs:
            if xStep == 0 and yStep == 0:
                continue
            x = i + xStep
            y = j + yStep
            while 0 <= x < len(seats) and 0 <= y < len(seats[x]) and seats[x][y] == '.':
                x += xStep
                y += yStep
            if 0 <= x < len(seats) and 0 <= y < len(seats[x]) and seats[x][y] == '#':
                count += 1
    return count

def partTwo (seatLayout):
    layout = deepcopy(seatLayout)

    while True:
        changed = False
        newLayout = deepcopy(layout)

        for i in range(0, len(layout)):
            for j in range(0, len(layout[i])):
                if layout[i][j] == '.':
                    continue
                adjacent = getVisible(layout, i, j)
                if adjacent == 0 and newLayout[i][j] != '#':
                    newLayout[i][j] = '#'
                    changed = True
                elif adjacent > 4 and newLayout[i][j] != 'L':
                    newLayout[i][j] = 'L'
                    changed = True
        if changed == False:
            break
        layout = newLayout
        
    getOccupied(layout)


# partOne(lines)
partTwo(lines)