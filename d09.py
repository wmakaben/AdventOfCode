file = open("input/d09.txt", 'r')

nums = [int(line.rstrip()) for line in file]
# preambleLen = 5
preambleLen = 25

def hasSum(idx):
    target = nums[idx + preambleLen]
    preamble = set()
    for i in range(idx, idx + preambleLen):
        if nums[i] != target/2 and target - nums[i] in preamble:
            return True
        preamble.add(nums[i])
    return False

# Part 1

# index = 0
# while hasSum(index):
#     index += 1
# print(nums[index + preambleLen])

# 15690279

# Part 2

# targetSum = 127
targetSum = 15690279
currSum = nums[0]
start = 0
end = 0

while currSum != targetSum:
    if currSum < targetSum:
        end += 1
        currSum += nums[end]
    elif currSum > targetSum:
        currSum -= nums[start]
        start += 1

numSubset = [nums[i] for i in range(start, end + 1)]
setMin = min(numSubset)
setMax = max(numSubset)
print(setMax + setMin)
