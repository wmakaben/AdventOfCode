from copy import deepcopy

file = open("input/d11.txt", 'r')
lines = [list(line.rstrip().replace("L", "#")) for line in file]

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

partOne(lines)


