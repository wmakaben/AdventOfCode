import re

# file = open("input/d12-ex.txt", 'r')
file = open("input/d12.txt", 'r')

def padState(state, pad):
	# The padding depends on the patterns
	# s = re.sub('^#', '.#', state)
	# s = re.sub('#$', '#...', s)
	return ('.' * pad) + state + ('.' * pad)

def stripState(state):
	s = re.sub('^\.+', '', state)
	s = re.sub('\.+$', '', s)
	return s

def getSum(state, offset):
	sum = 0
	for i in range(len(state)):
		if state[i] == '#':
			sum += i - offset
	return sum


state = file.readline().rstrip().split(" ")[2]

file.readline()

patterns = {}
for line in file:
	pattern = line.rstrip().split(" ")
	patterns[pattern[0]] = pattern[2]

padSize = 3
offset = 0
sum = 0
# gens = 50000000000
gens = 1000
print state
for g in range(0, gens):
	nextState = ""
	state = padState(state, padSize)
	offset += padSize
	for i in range (2, len(state) - 2):
		pattern = state[i-2:i+3]
		nextState += patterns.get(pattern, '.')
	state = nextState
	currSum = getSum(state, g)
	print str(g) + ": " + str(currSum) + "(" + str(currSum - sum) + ")"
	sum = currSum
# print stripState(state)
# print state
print getSum(state, gens)

# 1000: 97087 (+96)
print ((50000000000 - 1000) * 96) + 97087

