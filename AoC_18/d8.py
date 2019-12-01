# file = open("input/d8-ex.txt", 'r')
file = open("input/d8.txt", 'r')

def treeSum(tree, sum):
	childrenNum = int(tree.pop(0))
	metadataNum = int(tree.pop(0))
	for i in range(childrenNum):
		sum = treeSum(tree, sum)
	for i in range(metadataNum):
		sum += int(tree.pop(0))
	return sum

# Part 1
tree = file.readline().split(" ")
# print(treeSum(tree, 0))

# Part 2

def rootVal(tree):
	childrenNum = int(tree.pop(0))
	metadataNum = int(tree.pop(0))
	childrenVal = {}

	for i in range(childrenNum):
		childrenVal[i+1] = rootVal(tree)

	val = 0
	if childrenNum:
		for i in range(metadataNum):
			cIdx = int(tree.pop(0))
			if cIdx in childrenVal:
				val += childrenVal[cIdx]
	else:
		for i in range(metadataNum):
			val += int(tree.pop(0))
	return val

print rootVal(tree)