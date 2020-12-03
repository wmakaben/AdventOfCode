file = open("input/d02.txt", 'r')

def isValidCount (rule, letter, code):
    charCount = code.count(letter)
    return charCount >= rule[0] and charCount <= r
    
def isValidPosition (rule, letter, code):
    return (code[rule[0]-1] == letter or code[rule[1]-1] == letter) and code[rule[0]-1] != code[rule[1]-1]

valid = 0
for line in file:
    l = line.rstrip().split(' ')
    rule = [int(num) for num in l[0].split('-')]
    letter = l[1][0]
    code = l[2]

    # if isValidCount(rule, letter, code):
    #     valid += 1
    
    if isValidPosition(rule, letter, code):
        valid += 1

print(valid)



