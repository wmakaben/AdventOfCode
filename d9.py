import operator

# file = open("input/d9-ex.txt", 'r')
file = open("input/d9.txt", 'r')

input = file.readline().split(" ")
players = int(input[0])
lastMarble = int(input[6])# * 100

scores = {}
for player in range(0, players):
	scores[player] = 0

list = [0]
currIdx = 0
for i in range(1, lastMarble + 1):
	# print list
	if i % 23 == 0:
		player = (i - 1) % players
		scores[player] += i
		currIdx = (currIdx - 7) % len(list)
		scores[player] += list.pop(currIdx)
		currIdx = currIdx % len(list)
	else:
		currIdx = ((currIdx + 1) % len(list)) + 1
		# print currIdx
		list.insert(currIdx, i)
# print list
# print scores
print (max(scores.iteritems(), key=operator.itemgetter(1)))
