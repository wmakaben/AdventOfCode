# Iterate through dag, alphabetically

def getSteps(line):
	l = line.split(" ")
	return [l[1], l[7]]

def getSources(graph):
	sources = []
	for step in graph:
		if not len(graph[step]):
			sources.append(step)
	return sources

def initGraph(lines):
	graph = {}
	for line in file:
		step = getSteps(line)
		if step[0] not in graph:
			graph[step[0]] = {}
		if step[1] not in graph:
			graph[step[1]] = {}
		graph[step[1]][step[0]] = True
	return graph

def removeStep(graph, step):
	graph.pop(step, None)
	for s in graph.keys():
		graph[s].pop(step, None)
	return graph


# file = open("input/d7-ex.txt", 'r')
file = open("input/d7.txt", 'r')

graph = initGraph(file)
steps = graph.keys()
steps.sort()

order = ''
sources = []

# sources = getSources(graph)
# sources.sort()

# while len(sources):
# 	step = sources.pop(0)
# 	graph = removeStep(graph, step)
# 	sources = getSources(graph)
# 	sources.sort()
# 	order += step

# print order

# Part 2

stepVal = {}
for i in range(len(steps)):
	stepVal[steps[i]] = i + 1
valBase = 60
count = 0
wNum = 5
workers = {}

while len(graph) or len(workers):
	# Remove completed steps
	for k, v in workers.items():
		if v == 0:
			workers.pop(k)
			graph = removeStep(graph, k)
	# Add steps
	sources = getSources(graph)
	sources.sort()
	while len(workers) <= wNum and len(sources):
		step = sources.pop(0)
		workers[step] = stepVal[step] + valBase
		graph.pop(step, None)
	print workers
	# Increment count and decrement workers
	count += 1
	for k in workers.keys():
		workers[k] -= 1
	print workers
	print
print count

# TODO: answer was 931 (count - 1)

