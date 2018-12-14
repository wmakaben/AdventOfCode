file = open("input/d13-ex.txt", 'r')
# file = open("input/d13.txt", 'r')

'''
left = -1
straight = 0
right = 1

Cart map
key: [x,y]
value: [x, y, dirVal, intVal] 

intVal change at intersection
intVal = ((intVal + 2) % 3) - 1
'''

dirVal = { 0: '^', 1: '>', 2: 'v', 3: '<' }
dirSymbol = { '^': 0, '>': 1, 'v': 2, '<': 3 }
initTrack = { '>': '-', '<': '-', 'v': '|', '^': '|' }
dirChange = {
	'>': [1, 0],
	'v': [0, 1],
	'<': [-1, 0],
	'^': [0, -1]
}
trackVal = {
	'|': [0, 1],
	'-': [1, 0]
	# Get default is [1, 1]
}
dirSwitch = {
	'/': { '>': '^', '^': '>', '<': 'v', 'v': '<' },
	'\\': { '>': 'v', 'v': '>', '<': '^', '^': '<' },
}

def getIntChange (symbol, change):
	newSymbol = dirVal[(dirSymbol[symbol] + change) % 4]
	newChange = ((change + 2) % 4) - 1
	return [newSymbol, newChange]

carts = {}
tracks = []

y = 0
for line in file:
	x = 0
	trackRow = []
	for c in line.rstrip():
		trackRow.append(initTrack.get(c, c))
		if c in initTrack:
			carts[str([x,y])] = [x, y, c, -1]
		x += 1
	tracks.append(trackRow)
	# print ''.join(trackRow)
	y += 1

# print carts

crash = False
while not crash:
	newCarts = {}
	cartKeys = carts.keys()
	cartKeys.sort()
	for cartKey in cartKeys:
		cart = carts[cartKey]
		# Update position
		dVal = dirChange[cart[2]]
		tSymbol = tracks[cart[1]][cart[0]]
		tVal = trackVal.get(tSymbol, [1,1])
		newPos = [ cart[0] + (dVal[0] * tVal[0]), cart[1] + (dVal[1] * tVal[1]) ]
		# Look for crash
		newKey = str(newPos)
		if newKey in carts or newKey in newCarts:
			crash = True
			print newKey
			break
		# Update direction
		d = cart[2:]
		tSymbol = tracks[newPos[1]][newPos[0]]
		if tSymbol not in trackVal:
			# print newKey + ', ' + tSymbol
			if tSymbol in dirSwitch:
				d[0] = dirSwitch[tSymbol][d[0]]
			else:
				d = getIntChange(d[0], d[1])
		# print d
		newCarts[newKey] = [newPos[0], newPos[1]] + d
		carts.pop(cartKey)
	carts = newCarts
	print carts

