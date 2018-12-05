# Part 1
print "Part 1"

def getOppCase (c):
	if c.isupper():
		return c.lower()
	else:
		return c.upper()

file = open("input/d5.txt", 'r')
# file = open("input/d5-ex.txt", 'r')
line = file.readline()

# print line
for i in range(len(line) - 2, -1, -1):
	# print line[i]
	if line[i] == getOppCase(line[i+1]):
		line = line[:i] + line[i+2:]
		# print line
# print line
print len(line)