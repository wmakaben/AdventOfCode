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
sources = getSources(graph)
sources.sort()

while len(sources):
	step = sources.pop(0)
	graph = removeStep(graph, step)
	sources = getSources(graph)
	sources.sort()
	order += step

print order



