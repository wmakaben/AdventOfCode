file = open("input/d03.txt", 'r')

def getManhattanDist (p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def getSteps (p):
	pk = (p[0], p[1])
	return points[0][pk] + points[1][pk]

dirInc = {
	"U": [1, 1],
	"R": [0, 1],
	"D": [1, -1],
	"L": [0, -1]
}

points = [
	{ (0,0): 0 },
	{ (0,0): 0 }
]
intersections = []

def updatePoint (p, direction, distance, wireNum, step):
	for i in range(0, distance):
		step += 1
		p[dirInc[direction][0]] += dirInc[direction][1]

		pk = (p[0], p[1])
		if pk not in points[wireNum]:
			points[wireNum][pk] = step

		if wireNum == 1 and pk in points[0]:
			intersections.append(pk)
	return step

# file = ["R8,U5,L5,D3", "U7,R6,D4,L4"] # 6
# file = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"] # 159
# file = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"] # 135
# file = ["R3,U2,L2,D4", "D1,R1,U1"]

idx = 0
for line in file:
	wire = line.split(",")
	p = [0,0]
	step = 0
	for path in wire:
		direction = path[:1]
		distance = int(path[1:])
		step = updatePoint(p, direction, distance, idx, step)
	idx += 1

# print(intersections)
# print(min(getManhattanDist([0,0],d) for d in intersections))
print(min(getSteps(d) for d in intersections))
