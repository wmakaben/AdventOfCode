import re

file = open("input/d07.txt", 'r')

def buildGraph ():
    g = {}
    pattern = re.compile(r'([1-9]) ([a-z]+ [a-z]+) bag')

    for line in file:       
        # Get the container bag name
        container = " ".join(line.split(" ")[:2])
        if container not in g:
            g[container] = {}
        # Get bags in container bag
        for m in re.finditer(pattern, line):
            key = m.group(2)
            count = m.group(1)
            if key not in g:
                g[key] = {}
            g[key][container] = count
    return g

def getAncestors (key, visited=set()):
    for parent in graph[key].keys():
        if parent not in visited:
            visited.add(parent)
            getAncestors(parent, visited)
    return visited

# Uncomment for Part 1
# graph = buildGraph()
# ancestors = getAncestors("shiny gold")
# print(ancestors)
# print(len(ancestors))

# Part 2

def buildAnotherGraph ():
    g = {}
    pattern = re.compile(r'([1-9]) ([a-z]+ [a-z]+) bag')

    for line in file:       
        # Get the container bag name
        container = " ".join(line.split(" ")[:2])
        if container not in g:
            g[container] = {}
        # Get bags in container bag
        for m in re.finditer(pattern, line):
            key = m.group(2)
            count = m.group(1)
            if key not in g:
                g[key] = {}
            g[container][key] = int(count)
    return g

def getDescendantCount (key, counts={}):
    c = 1
    for child, num in graph[key].items():
        if child in counts:
            c += num * counts[child]
            print(key, c)
        else:
            c += num * getDescendantCount(child, counts)
            print(key, c)
    print(key, c)
    counts[key] = c
    return c

graph = buildAnotherGraph()
cnts = {}
print(getDescendantCount("shiny gold", cnts) - 1)
print(cnts)