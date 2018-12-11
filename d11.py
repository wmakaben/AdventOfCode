def getCellVal(x, y, num):
	rackId = x + 10
	powerLevel = ((rackId * y) + num) * rackId
	level = 0
	if powerLevel > 99:
		level = int(str(powerLevel)[-3])
	return level - 5

def initGrid(size, serialNum):
	grid = []
	for i in range(1, size + 1):
		grid.append([])
		for j in range(1, size + 1):
			grid[i-1].append(getCellVal(i, j, serialNum))
	return grid

def subGridSum(grid, x, y, area):
	sum = 0
	for i in range(x, x + area):
		for j in range(y, y + area):
			sum += grid[i][j]
	return sum


gridSerialNum = 8199
# gridSerialNum = 57
gridSize = 300
areaStart = 21
areaEnd = 30
# areaSize = 3

# Note - when accessing values from grid, get value at [x-1][y-1] 

grid = initGrid(gridSize, gridSerialNum)

maxSum = -1000000
maxX = 0
maxY = 0
maxA = 0
for a in range(areaStart, areaEnd + 1):
	for i in range(0, len(grid) - a):
		for j in range(0, len(grid) - a):
			sum = subGridSum(grid, i, j, a)
			# print sum
			if sum > maxSum:
				maxSum = sum
				maxX = i
				maxY = j
				maxA = a
print maxSum
print str(maxX+1) + ", " + str(maxY+1) + ", " + str(maxA)


# 10-20 18	119
# 21-30 21 	91

