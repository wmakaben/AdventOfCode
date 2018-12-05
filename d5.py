# Part 1
print "Part 1"

def getOppCase (c):
	if c.isupper():
		return c.lower()
	else:
		return c.upper()

def react (p):
	for i in range(len(p) - 2, -1, -1):
		if i+1 < len(p) and p[i] == getOppCase(p[i+1]):
			p = p[:i] + p[i+2:]
	return len(p)

# file = open("input/d5-ex.txt", 'r')
file = open("input/d5.txt", 'r')
line = file.readline()
print react(line)

# Part 2
print "Part 2"

charSet = set(line.lower())
length = len(line)
# print line
for c in charSet:
	# print c
	tmpLine = line.replace(c, "").replace(c.upper(), "")
	# print tmpLine
	length = min(length, react(tmpLine))
print length
