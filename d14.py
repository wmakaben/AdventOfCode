'''
Starts with 2 recipes
- new recipes from digits of sum of current
- add new to end of list
- each elf moves 1 + current recipe score (looping)
after 846601
'''

n = 846601
# n = 5
# recipes = [3, 7]
recipes = '37'
e1 = 0
e2 = 1

# while len(recipes) < n + 10:
while str(n) not in recipes[-7:]:
	# recipes += map(int, list(str(recipes[e1] + recipes[e2])))
	# e1 = (e1 + 1 + recipes[e1]) % len(recipes)
	# e2 = (e2 + 1 + recipes[e2]) % len(recipes)
	recipes += str(int(recipes[e1]) + int(recipes[e2]))
	e1 = (e1 + 1 + int(recipes[e1])) % len(recipes)
	e2 = (e2 + 1 + int(recipes[e2])) % len(recipes)

# print ''.join(map(str, recipes[n:n+10]))
# print ''.join(recipes[n:n+10])

# print len(recipes)
# print recipes[-7:]

print len(recipes) - 7 + recipes[-7:].index(str(n))
