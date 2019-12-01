import re

# file = open("input/d10-ex.txt", 'r')
file = open("input/d10.txt", 'r')

def parseLine(line):
	return map(int, re.findall(r'-?\d+', line))

def getKey(x, y):
	return str(x) + "," + str(y)

def updateBounds(bounds, point):
	bounds[0] = min(bounds[0], point[0])
	bounds[1] = min(bounds[1], point[1])
	bounds[2] = max(bounds[2], point[0])
	bounds[3] = max(bounds[3], point[1])

def printMap(posMap, bounds):
	for i in range(bounds[0], bounds[2] + 1):
		for j in range(bounds[1], bounds[3] + 1):
			if getKey(i, j) in posMap:
				print "X",
			else:
				print " ",
		print

# TODO: filter by character height bounds?
skip = 10629
end = 10630

lights = []
for line in file:
	light = parseLine(line)
	light[0] += light[2] * skip
	light[1] += light[3] * skip
	lights.append(light)

for i in range(skip, end):
	bounds = [1000000, 10000000, -10000000, -10000000]
	posMap = {}
	for light in lights:
		light[0] += light[2]
		light[1] += light[3]
		posMap[getKey(light[0], light[1])] = True
		updateBounds(bounds, light)
	if bounds[3] - bounds[1] < 10:
		print i + 1
		print bounds
		print
		printMap(posMap, bounds)
		print
