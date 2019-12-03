file = open("input/d03.txt", 'r')

def getManhattanDist (p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

dirInc = {
	"U": [1, 1],
	"R": [0, 1],
	"D": [1, -1],
	"L": [0, -1]
}
points = { 0: { 0: 1 } }
intersections = []

def updatePoint (p, direction, distance, first):
	for i in range(0, distance):
		p[dirInc[direction][0]] += dirInc[direction][1]
		if p[0] not in points:
			points[p[0]] = {}
		if p[1] not in points[p[0]]:
			points[p[0]][p[1]] = 0
		if not first and points[p[0]][p[1]] == 1:
			# print(p)
			intersections.append(p.copy())
		else:
			points[p[0]][p[1]] += 1

# file = ["R8,U5,L5,D3", "U7,R6,D4,L4"] # 6
# file = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"] # 159
# file = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"] # 135

first = True
for line in file:
	wire = line.split(",")
	p = [0,0]
	for path in wire:
		direction = path[:1]
		distance = int(path[1:])
		updatePoint(p, direction, distance, first)
	first = False

print(intersections)
print(min(getManhattanDist([0,0],d) for d in intersections))