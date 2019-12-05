file = open("input/d05.txt", 'r')
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


def runProg (code):
	i = 0
	while True:
		op = code[i]	
		# print(op)

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
			print("input: ")
			val = input()
			p = getInParams(code, i)
			code[p] = int(val)
			i += 2
		elif op in outOps:
			p = getInParams(code, i)
			print(code[p])
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
	return code[0]

runProg(intcode)

# icode = [1002,4,3,4,33]
# icode = [3,9,8,9,10,9,4,9,99,-1,8]
# icode = [3,9,7,9,10,9,4,9,99,-1,8]
# icode = [3,3,1108,-1,8,3,4,3,99]
# icode = [3,3,1107,-1,8,3,4,3,99]
# icode = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
# icode = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
# icode = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
# runProg(icode)
# print(icode)