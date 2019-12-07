from itertools import permutations

file = open("input/d07.txt", 'r')
intcode = list(map(int, file.readline().split(",")))

exitOp = {99}
addOps = {1, 101, 1001, 1101}#, 10001, 10101, 11001, 11101}
multOps = {2, 102, 1002, 1102}#, 10002, 10102, 11002, 11102}
inOps = {3, 103}
outOps = {4, 104}
jtOps = {5, 105, 1005, 1105}
jfOps = {6, 106, 1006, 1106}
ltOps = {7, 107, 1007, 1107}
eqOps = {8, 108, 1008, 1108}

def get_digit(number, n):
	return number // 10**n % 10

def getMathParams(code, i):
	op = code[i]
	p1 = code[i+1]
	if get_digit(op, 2) == 0:
		p1 = code[code[i+1]]
	p2 = code[i+2]
	if get_digit(op, 3) == 0:
		p2 = code[code[i+2]]
	p3 = i+3
	if get_digit(op, 4) == 0:
		p3 = code[p3]
	return (p1,p2,p3)

def getInParams(code, i):
	op = code[i]
	p = i + 1
	if get_digit(op, 2) == 0:
		p =  code[p]
	return p

def getJumpParams(code, i):
	op = code[i]
	p1 = code[i+1]
	if get_digit(op, 2) == 0:
		p1 = code[code[i+1]]
	p2 = code[i+2]
	if get_digit(op, 3) == 0:
		p2 = code[code[i+2]]
	return (p1,p2)

def runProg (code, params, idx):
	paramCount = 0
	outputSignal = None
	i = idx[0]
	while True:
		op = code[i]	
		if op in exitOp:
			break
		elif op in addOps:
			p = getMathParams(code, i)
			code[p[2]] = p[0] + p[1]
			i += 4
		elif op in multOps:
			p = getMathParams(code, i)
			code[p[2]] = p[0] * p[1]
			i += 4
		elif op in inOps:
			if paramCount >= len(params):
				break
			val = params[paramCount]
			paramCount += 1
			# val = input()
			p = getInParams(code, i)
			code[p] = int(val)
			i += 2
		elif op in outOps:
			# Assumes this only outputs once per amplifier "session"
			p = getInParams(code, i)
			outputSignal = code[p]
			i += 2
		elif op in jtOps:
			p = getJumpParams(code, i)
			i = p[1] if p[0] != 0 else i + 3
		elif op in jfOps:
			p = getJumpParams(code, i)
			i = p[1] if p[0] == 0 else i + 3
		elif op in ltOps:
			p = getMathParams(code, i)
			code[p[2]] = 1 if p[0] < p[1] else 0
			i += 4
		elif op in eqOps:
			p = getMathParams(code, i)
			code[p[2]] = 1 if p[0] == p[1] else 0
			i += 4
	idx[0] = i
	return outputSignal

def getSignal(settings):
	codeState = {}
	codeIdx = {}
	signal = None
	currentSignal = 0

	sIdx = 0
	while currentSignal != None:
		setting = settings[sIdx]
		params = []
		if setting not in codeState:
			codeState[setting] = intcode.copy()
			codeIdx[setting] = [0]
			params.append(setting)
		params.append(currentSignal)
		currentSignal = runProg(codeState[setting], params, codeIdx[setting])

		if currentSignal == None:
			break

		sIdx += 1
		if sIdx >= len(settings):
			signal = currentSignal
			sIdx = sIdx % len(settings)

	# for setting in settings:
	# 	if setting not in codeState:
	# 		codeState[setting] = intcode.copy()
	# 		codeIdx[setting] = 0
	# 	currentSignal = runProg(codeState[setting], [setting, currentSignal], codeIdx[setting])
	return signal

# Part 1 Tests:
# intcode = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# settings = [4,3,2,1,0]
# intcode = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
# settings = [0,1,2,3,4]
# intcode = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
# settings = [1,0,4,3,2]
# print(getSignal(settings))

# Part 1 Solution:
# settingsOptions = list(permutations(range(0,5)))
# print(max(getSignal(s) for s in settingsOptions))

# Part 2 Tests:
# intcode = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
# settings = [9,8,7,6,5]
# intcode = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
# settings = [9,7,8,5,6]
# print(getSignal(settings))

# Part 2 Solution:
settingsOptions = list(permutations(range(5,10)))
print(max(getSignal(s) for s in settingsOptions))
