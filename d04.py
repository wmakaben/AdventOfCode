import re

file = open("input/d04.txt", 'r')

validEcl = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def isBetween(value, min, max):
    return min <= int(value) <= max

def isValidHgt (hgt):
    hgtRegex = re.compile(r'(^\d{2,3})(in|cm)$')
    hgtMatch = hgtRegex.search(hgt)
    if hgtMatch is None:
        return False
    unit = hgtMatch.group(2)
    value = hgtMatch.group(1)
    if unit == 'cm' and not isBetween(value, 150, 193):
        return False
    elif unit == 'in' and not isBetween(value, 59, 76):
        return False
    return True

def isValidHcl (hcl):
    hclRegex = re.compile(r'(^#[0-9a-f]{6}$)')
    hclMatch = hclRegex.search(hcl)
    return hclMatch is not None

def isValidPid (pid):
    pidRegex = re.compile(r'(^[0-9]{9}$)')
    pidMatch = pidRegex.search(pid)
    return pidMatch is not None

def isValid (cred):
    # Assumptions:
    # All byr, iyr, and eyr values are numbers
    if not isBetween(cred['byr'], 1920, 2002):
        return False
    elif not isBetween(cred['iyr'], 2010, 2020):
        return False
    elif not isBetween(cred['eyr'], 2020, 2030):
        return False
    elif not isValidHgt(cred['hgt']):
        return False
    elif not isValidHcl(cred['hcl']):
        return False
    elif cred['ecl'] not in validEcl:
        return False
    elif not isValidPid(cred['pid']):
        return False
    return True

cred = {}
valid = 0
# 
for line in file:
    line = line.rstrip()
    if line == '':
        fieldNum = len(cred)
        # Assumes all the fields are found in the set of passport fields
        if fieldNum >= 8 and isValid(cred):
            valid += 1
        elif fieldNum == 7 and 'cid' not in cred and isValid(cred):
            valid += 1
        cred = {}
    else:
        for data in line.split(' '):
            field = data.split(':')
            cred[field[0]] = field[1]

print(valid)