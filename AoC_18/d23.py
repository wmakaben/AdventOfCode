# file = open("input/d23-ex.txt", 'r')
file = open("input/d23.txt", 'r')

def formatBot(line):
	line = line.replace('pos=<', '').replace('>, r=', ' ').rstrip()
	line = line.split(' ')
	line[0] = map(int, line[0].split(','))
	line[1] = int(line[1])
	return line

def getDist(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])

bots = []
idx = -1
maxRad = -1
count = 0
for line in file:
	bot = formatBot(line)
	if bot[1] > maxRad:
		idx = count
		maxRad = bot[1]
	bots.append(bot)
	count += 1

for b in bots: 
	print b
print
print idx
print bots[idx]
print

count = 0
for bot in bots:
	if getDist(bot[0], bots[idx][0]) <= bots[idx][1]:
		count += 1
print count