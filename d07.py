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

def runProg (icode, params):
	code = icode.copy()
	paramCount = 0
	outputSignal = None
	i = 0
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
			# print("input: ")
			val = params[paramCount]
			paramCount += 1
			# val = input()
			p = getInParams(code, i)
			code[p] = int(val)
			i += 2
		elif op in outOps:
			p = getInParams(code, i)
			# print(code[p])
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
	# return code[0]
	return outputSignal

# intcode = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# settings = [4,3,2,1,0]
# intcode = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
# settings = [0,1,2,3,4]
# intcode = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
# settings = [1,0,4,3,2]

def getSignal(settings):
	signal = 0
	for setting in settings:
		signal = runProg(intcode, [setting, signal])
	return signal

from itertools import permutations
settingsOptions = list(permutations(range(0,5)))
print(len(settingsOptions))

print(max(getSignal(s) for s in settingsOptions))



