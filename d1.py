file = open("input/d1.txt", 'r')

# Part 1

num = 0
for x in file:
	num = num + float(x)
print num

# Part 2

d = {}
f = 0

while f not in d or d[f] != 2:
	file = open("input/d1.txt", "r")
	for n in file:
		f += float(n)
		if f in d:
			d[f] += 1
			if d[f] == 2:
				break
		else:
			d[f] = 1
print f

