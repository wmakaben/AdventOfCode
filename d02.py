file = open("input/d02.txt", 'r')
intcode = list(map(int, file.readline().split(",")))

# test = "1,9,10,3,2,3,11,0,99,30,40,50"
# test = "1,0,0,0,99" # becomes 2,0,0,0,99
# test = "2,3,0,3,99" # becomes 2,3,0,6,99 (3 * 2 = 6).
# test = "2,4,4,5,99,0" # becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
# test = "1,1,1,4,99,5,6,0,99" # becomes 30,1,1,4,2,5,6,0,99.
# code = list(map(int, test.split(",")))

def runProg (intcode, noun, verb):
	code = intcode.copy()
	code[1] = noun
	code[2] = verb
	i = 0
	while True:
		if code[i] == 99:
			break
		elif code[i] == 1:
			code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]]
		elif code[i] == 2:
			code[code[i + 3]] = code[code[i + 1]] * code[code[i + 2]]
		i += 4
	return code[0]

print(runProg(intcode, 12, 2))
# 6327510


# Part 2
for i in range(100):
	for j in range(100):
		if (runProg(intcode, i, j) == 19690720):
			print(100 * i + j)
			break