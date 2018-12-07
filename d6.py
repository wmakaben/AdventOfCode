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

def getClosestPoint (p, pList):
	multi = False
	dist = getManhattanDist(p, pList[0])
	idx = 0
	# print str(p) + " => " + str(pList[0]) + "\t" + str(dist)
	for i in range(1, len(pList)):
		d = getManhattanDist(p, pList[i])
		# print str(p) + " => " + str(pList[i]) + "\t" + str(d)
		if d < dist:
			dist = d
			idx = i
			multi = False
		elif d == dist:
			multi = True
	if multi:
		return "."
	return idx

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

count = {}
for i in range(0, len(points)):
	count[i] = 0

for i in range(bMin[1], bMax[1] + 1):
	m[bMin[0]][i] = getClosestPoint([bMin[0],i], points)
	count.pop(m[bMin[0]][i], None)
	m[bMax[0]][i] = getClosestPoint([bMax[0],i], points)
	count.pop(m[bMax[0]][i], None)

for i in range(bMin[0] + 1, bMax[0]):
	m[i][bMin[1]] = getClosestPoint([i, bMin[1]], points)
	count.pop(m[i][bMin[1]], None)
	m[i][bMax[1]] = getClosestPoint([i, bMax[1]], points)
	count.pop(m[i][bMax[1]], None)

for i in range(bMin[0] + 1, bMax[0]):
	for j in range(bMin[1] + 1, bMax[1]):
		m[i][j] = getClosestPoint([i,j], points)
		if m[i][j] in count:
			count[m[i][j]] += 1

# printMap(m)
print count
pMax = (max(count.iteritems(), key=operator.itemgetter(1))[0])
print str(pMax) + ": " + str(count[pMax])

'''
Possible dynamic approach
- Move in direction (up, right, down, left)
  - if has closestPoint > -1, stop direction
  - else if out of bounds, break out of search for point (return -1 as the count)
  - else get closest point
  	- keep going if current point is closest
'''

# def countArea (map, point, count, pIdx):
	# if m[p[0]][p[1]] >= -1:
	# 	return [m, p, c]
