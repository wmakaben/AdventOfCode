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

print("Part 1")
if n[i] + n[j] == target:
    print(n[i] * n[j])
else:
    print("Nope")

# Part 2

k = 0
s = n[i] + n[j] + n[k]
while s != target and k < i and i < j:
    s = n[i] + n[j] + n[k]
    if s > target and i + 1 < j:
        j -= 1
    elif s > target and i + 1 == j:
        i -= 1
    elif s < target and k + 1 < i:
        k += 1
    elif s < target and k + 1 == i:
        i += 1

print("Part 2")
if s == target:
    print(n[i] * n[j] * n[k])
else:
    print("Nope")