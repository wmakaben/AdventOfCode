file = open("input/d01.txt", 'r')

def getFuel(mass):
	return (mass // 3) - 2

totalFuel = 0
for mass in file:
	totalFuel = totalFuel + getFuel(int(mass))

# Test Case: 654, 966
# totalFuel = getFuel(1969)
# Test Case: 33583, 50346
# totalFuel = getFuel(100756)

print(totalFuel)
# 3231941