import operator
# Part 1

file = open("input/d4.txt", 'r')
# file = open("input/d4-ex.txt", 'r')
events = file.read().splitlines()
events.sort()


guards = {}
guardTotal = {}
currentGuard = None
sleepStart = None

for evt in events:
	if "Guard" in evt:
		currentGuard = evt.split(" ")[3][1:]
	elif "falls" in evt:
		sleepStart = int(evt.split(" ")[1][3:][:-1])
	elif "wakes" in evt:
		wakeTime = int(evt.split(" ")[1][3:][:-1])
		for i in range(sleepStart, wakeTime):
			if currentGuard not in guards:
				guards[currentGuard] = {}
				guardTotal[currentGuard] = 0
			if i not in guards[currentGuard]:
				guards[currentGuard][i] = 0
			guards[currentGuard][i] += 1
			guardTotal[currentGuard] += 1

guard = max(guardTotal.iteritems(), key=operator.itemgetter(1))[0]
print guard
minute = max(guards[guard].iteritems(), key=operator.itemgetter(1))[0]
print minute
print int(guard) * int(minute)

# Part 2
print "\nPart 2"

g = {}
m = {}
for k, v in guards.iteritems():
	g[k] = max(guards[k].iteritems(), key=operator.itemgetter(1))[0]
	m[k] = guards[k][g[k]]
print g
print m

guard = max(m.iteritems(), key=operator.itemgetter(1))[0]
print guard
minute = g[guard]
print minute
print int(guard) * int(minute)