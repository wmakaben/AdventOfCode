# file = open("input/d25-ex.txt", 'r')
file = open("input/d25.txt", 'r')

def getDist (p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]) + abs(p1[3] - p2[3])

def getConnectedPoints (graph, point, connected):
	connected[point] = True
	while len(graph[point]):
		p = graph[point].keys()[0]
		graph[point].pop(p)
		graph[p].pop(point)
		if p not in connected:
			connected = getConnectedPoints(graph, p, connected)
	graph.pop(point)
	return connected

points = []
graph = {}

# Get list of points from input
for line in file:
	point = map(int, line.rstrip().split(','))
	points.append(point)
	graph[str(point)] = {}

# Build a graph where points are nodes and edges connect nodes within a manhattan distance of 3
for i in range(len(points) - 1):
	for j in range(i + 1, len(points)):
		if getDist(points[i], points[j]) < 4:
			p1 = str(points[i])
			p2 = str(points[j])
			graph[p1][p2] = True
			graph[p2][p1] = True

# Find all disconnected graph parts (I think it's called forests or something)
count = 0
while len(graph) > 0:
	point = graph.keys()[0]
	print getConnectedPoints(graph, point, {})
	count += 1
print count