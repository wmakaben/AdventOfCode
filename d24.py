import operator
import math

# file = open("input/d24-ex.txt", 'r')
file = open("input/d24.txt", 'r')

'''
	Group object format
	[units, hp, immune, weak, damage, damage_type, init, isInfection]
	0 - id
	1 - is infection
	2 - units
	3 - hp
	4 - immune
	5 - weak
	6 - damage
	7 - damage type
	8 - initiative
'''
immune = {}
infection = {}

def formatStatus(line):
	line = line[2:]
	statuses = {}
	if line:
		line = line.split(',')
		for status in line:
			statuses[status] = True
	return statuses

def formatGroup(line, id, isInfection, boost):
	group = line.split(' ')
	group[0] = int(group[0])
	group[1] = int(group[1])
	group[2] = formatStatus(group[2])
	group[3] = formatStatus(group[3])
	group[4] = int(group[4]) + boost
	group[6] = int(group[6])
	group.insert(0, id)
	group.insert(1, isInfection)
	return group

'''
Target selection:
- Sort groups by effective power, then initiative
- Find opposing untargeted group that a group would damage the most (accounting for weak/immune)
	- Break tie by effective power, then init
	- Must have units
'''

def getGroupById(groupId):
	return immune.get(groupId, infection.get(groupId))

def getPower(group):
	return group[2] * group[6]

def calculateDamage(g1, g2):
	if g1[7] in g2[4]:
		return 0
	elif g1[7] in g2[5]:
		return getPower(g1) * 2
	else:
		return getPower(g1)

def isNewTarget(t, tDmg, g, gDmg):
	# Compare damage, power, then init
	return gDmg > tDmg or (gDmg == tDmg and getPower(g) > getPower(t)) or (gDmg == tDmg and getPower(g) == getPower(t) and g[8] > t[8])

def findTarget(group, untargeted):
	groups = untargeted[0] if group[1] else untargeted[1]
	enemies = groups.values()
	if len(enemies):
		target = enemies[0]
		targetDamage = calculateDamage(group, target)
		for i in range(1, len(enemies)):
			enemy = enemies[i]
			damage = calculateDamage(group, enemy)
			if isNewTarget(target, targetDamage, enemy, damage):
				target = enemy
				targetDamage = damage
		if targetDamage > 0:
			return groups.pop(target[0])

def selectTargets():
	targets = {}
	untargeted = [immune.copy(), infection.copy()]
	groups = immune.values() + infection.values()
	for group in groups:
		if len(group) <= 9:
			group.append(0)
		group[9] = getPower(group)
	groups = sorted(groups, key=operator.itemgetter(9, 8), reverse=True)
	for g in groups:
		if g[2]:
			target = findTarget(g, untargeted)
			if target:
				targets[g[0]] = target[0]
	return targets

def attackTarget(group, targetId):
	target = getGroupById(targetId)
	damage = calculateDamage(group, target)
	unitsKilled = min(int(damage / target[3]), target[2])
	target[2] = target[2] - unitsKilled

def attack(targets):
	groups = immune.values() + infection.values()
	groups = sorted(groups, key=operator.itemgetter(8), reverse=True)
	for g in groups:
		if g[2] and g[0] in targets:
			attackTarget(g, targets[g[0]])

def filterGroups(groups):
	return {k:v for k,v in groups.iteritems() if v[2] > 0}

def getUnitSum(groups):
	sum = 0
	for k,v in groups.iteritems():
		sum += v[2]
	return sum

army = immune
count = 0
# 30 - 42
boost = 43
# boost = 1570
isInfection = False
for line in file:
	if 'Infection' in line:
		army = infection
		isInfection = True
		boost = 0
	else:
		army[count] = formatGroup(line.rstrip(), count, isInfection, boost)
		count += 1

while len(immune) != 0 and len(infection) != 0:
	targets = selectTargets()
	attack(targets)
	immune = filterGroups(immune)
	infection = filterGroups(infection)
	# print immune
	# print infection
	print "Total Units: " + str(getUnitSum(immune) + getUnitSum(infection))
	# print "Immune System: " + str(len(immune)) + ", Infection: " + str(len(infection))
	print len(immune) > 0
	print

# part 1: 16678
