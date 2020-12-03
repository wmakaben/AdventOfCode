file = open("input/d01.txt", 'r')

n = [int(line.rstrip()) for line in file]
n.sort()

target = 2020
i = 0
j = len(n) - 1

while n[i] + n[j] != target and i < j:
    if n[i] + n[j] < target:
        i += 1
    elif n[i] + n[j] > target:
        j -= 1

if n[i] + n[j] == target:
    print(n[i] * n[j])
else:
    print("Nope")