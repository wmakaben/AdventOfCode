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

tree = file.readline().split(" ")
print(treeSum(tree, 0))
