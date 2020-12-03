file = open("input/d01.txt", 'r')

def getFuel(mass):
	return (mass // 3) - 2

totalFuel = 0
for mass in file:
	totalFuel = totalFuel + getFuel(int(mass))

# Test Case: 654
# totalFuel = getFuel(1969)
# Test Case: 33583
# totalFuel = getFuel(100756)

print(totalFuel)
# 3231941

# Part 2

file = open("input/d01.txt", 'r')

totalFuel = 0
for mass in file:
	fuel = getFuel(int(mass))
	while fuel > 0:
		totalFuel += fuel
		fuel = getFuel(fuel)

print(totalFuel)
# 4845049