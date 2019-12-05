file = open("input/d05.txt", 'r')
intcode = list(map(int, file.readline().split(",")))

# TODO: params for writing positions can't be in immediate mode, so this might need to be adjusted
exitOp = {99}
addOps = {1, 101, 1001, 1101, 10001, 10101, 11001, 11101}
multOps = {2, 102, 1002, 1102, 10002, 10102, 11002, 11102}
inOps = {3, 103}
outOps = {4, 104}

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
	return code[0]

runProg(intcode)

# icode = [1002,4,3,4,33]
# runProg(icode)
# print(icode)
