# Part 1

def parseOffset(offsetStr):
	return [int(x) for x in offsetStr[:len(offsetStr) - 1].split(",")]

def parseDim(dimStr):
	return [int(x) for x in dimStr.split("x")]


file = open("input/d3.txt", 'r')
fabric = {}

for line in file.read().splitlines():
	input = line.split(" ")
	offset = parseOffset(input[2])
	dim = parseDim(input[3])

	for i in range(offset[0], offset[0] + dim[0]):
		for j in range(offset[1], offset[1] + dim[1]):
			if i not in fabric:
				fabric[i] = {}

			if j not in fabric[i]:
				fabric[i][j] = 1
			else:
				fabric[i][j] += 1

count = 0
for row, columns in fabric.items():
	for column, uses in columns.items():
		if uses > 1:
			count += 1
print count

# Part 2

file = open("input/d3.txt", 'r')
# Yep, brute force forever
for line in file.read().splitlines():
	input = line.split(" ")
	offset = parseOffset(input[2])
	dim = parseDim(input[3])

	clean = True
	for i in range(offset[0], offset[0] + dim[0]):
		for j in range(offset[1], offset[1] + dim[1]):
			if fabric[i][j] > 1:
				clean = False
				break

	if clean:
		print input
		break
