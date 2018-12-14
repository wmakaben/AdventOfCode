import numpy as np

# file = open("input/d13-ex.txt", 'r')
# file = open("input/d13-ex-2.txt", 'r')
file = open("input/d13.txt", 'r')

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

initTrack = { '>': '-', '<': '-', 'v': '|', '^': '|' }
initDir = { '^': 0, '>': 1, 'v': 2, '<': 3 }
# 		   ^				  >					v 				  <
dirMove = [np.array([0, -1]), np.array([1, 0]), np.array([0, 1]), np.array([-1, 0])]
trackMove = {'|': np.array([0, 1]), '-': np.array([1, 0])}
cornerDirections = {
	# 0 - 1, 2 - 3
	# '/': { '>': '^', '^': '>', '<': 'v', 'v': '<' },
	'/': [1,0,3,2],
	# 1 - 2, 3 - 0
	# '\\': { '>': 'v', 'v': '>', '<': '^', '^': '<' }
	'\\': [3,2,1,0]
}


def init (lines, carts, tracks):
	y = 0
	for line in lines:
		x = 0
		row = []
		for c in line.rstrip():
			row.append(initTrack.get(c, c))
			if c in initDir:
				carts[str([x,y])] = [np.array([x,y]), initDir[c], -1]
			x += 1
		tracks.append(row)
		y += 1

def moveCart (cart, track):
	cart[0] += (dirMove[cart[1]] * trackMove.get(track, np.array([1,1])))

def turnCart (cart, track):
	if track == '+':
		cart[1] = (cart[1] + cart[2]) % 4
		cart[2] = ((cart[2] + 2) % 3) - 1
	elif track in cornerDirections:
		cart[1] = cornerDirections[track][cart[1]]

carts = {}
tracks = []
init(file, carts, tracks)

crash = False
while not crash:
	for cartKey in sorted(carts):
		cart = carts[cartKey]
		track = tracks[cart[0][1]][cart[0][0]]
		moveCart(cart, track)
		newCartKey = str(cart[0])

		if newCartKey in carts:
			crash = True
			print newCartKey
			break

		track = tracks[cart[0][1]][cart[0][0]]
		turnCart(cart, track)
		carts[newCartKey] = carts.pop(cartKey)



