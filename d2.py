# Part 1
def getCount(id):
	charCount = {}
	countGroup = {2: False, 3: False}

	for c in id:
		if c in charCount:
			charCount[c] += 1
		else:
			charCount[c] = 1

	for k, v in charCount.items():
		if v == 2:
			countGroup[2] = True
		elif v == 3:
			countGroup[3] = True
		if countGroup[2] and countGroup[3]:
			break

	return countGroup 

file = open("input/d2.txt", 'r')
twoCount = 0
threeCount = 0
for line in file:
	group = getCount(line)
	if group[2]:
		twoCount += 1
	if group[3]:
		threeCount += 1
print twoCount * threeCount

# Part 2
def stringDiff(str1, str2):
	diffCount = 0
	diffIdx = 0
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			diffCount += 1
			if diffCount > 1:
				break
			diffIdx = i
	if diffCount == 1:
		print str1
		print str2
		return str1[:diffIdx] + str1[diffIdx+1:]
	else:
		return ""

file = open("input/d2.txt", 'r')
ids = file.read().splitlines()
for i in range(len(ids)):
	for j in range(i+1, len(ids)):
		id = stringDiff(ids[i], ids[j])
		if id != "":
			print id
			break



