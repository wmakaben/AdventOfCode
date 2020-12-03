file = open("input/d02.txt", 'r')

valid = 0
for line in file:
    l = line.rstrip().split(' ')
    rule = [int(num) for num in l[0].split('-')]
    letter = l[1][0]
    code = l[2]

    charCount = code.count(letter)
    if charCount >= rule[0] and charCount <= rule[1]:
        valid += 1

print(valid)



