import operator

def convertToCoord (line):
	return [int(n) for n in line.replace(" ", "").strip().split(',')]

def printMap (m):
	for i in range(len(m[0])):
		for j in range(len(m)):
			print m[j][i],
		print

def getManhattanDist (p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def getPointDist(p, pList):
	dist = 0
	for i in range(0, len(pList)):
		dist += getManhattanDist(p, pList[i])
	return dist

# file = open("input/d6-ex.txt", 'r')
file = open("input/d6.txt", 'r')

coord = convertToCoord(file.next())
points = [coord]
bMin = [coord[0], coord[1]]
bMax = [coord[0], coord[1]]

for line in file:
	coords = convertToCoord(line)
	points.append(coords)
	bMin[0] = min(coords[0], bMin[0])
	bMin[1] = min(coords[1], bMin[1])
	bMax[0] = max(coords[0], bMax[0])
	bMax[1] = max(coords[1], bMax[1])

m = [["."]*(bMax[1]+1) for i in range(bMax[0]+1)]
count = 0

for i in range(bMin[0], bMax[0] + 1):
	for j in range(bMin[1], bMax[1] + 1):
		d = getPointDist([i,j], points)
		# if d < 32:
		if d < 10000:
			m[i][j] = "#"
			count += 1
		else:
			m[i][j] = "."

# printMap(m)
print count
