file = open("input/d06.txt", 'r')

graph = {}
for line in file:
	orbit = line.rstrip().split(")")
	graph[orbit[1]] = orbit[0]

def getOrbits(g, key, total, visited):
	if key in visited:
		return visited[key]
	elif key not in g:
		visited[key] = 0
		return visited[key]
	else:
		visited[key] = 1 + getOrbits(g, g[key], total, visited)
		total[0] += visited[key]
		return visited[key]

totalOrbits = [0]
orbits = {}
for k in graph.keys():
	getOrbits(graph, k, totalOrbits, orbits)
# print(orbits)
print(totalOrbits)

# Part 2

# TODO: find most common ancestor between YOU and SAN
# - Get ancestor by tree level (# of orbits)
y = graph["YOU"]
s = graph["SAN"]
steps = 0
while y != s:
	if orbits[y] <= orbits[s]:
		s = graph[s]
		steps += 1
	elif orbits[s] < orbits[y]:
		y = graph[y]
		steps += 1
print(steps)