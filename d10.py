file = open("input/d10.txt", 'r')

nums = [int(line.rstrip()) for line in file]
nums.sort()
nums.insert(0, 0)
nums.append(nums[len(nums) - 1] + 3)
print(nums)

# Part 1
# diffs = {}
# for i in range(1, len(nums)):
#     diff = nums[i] - nums[i-1]
#     print(nums[i], diff)
#     if diff not in diffs:
#         diffs[diff] = 0
#     diffs[diff] += 1

# print(diffs)
# print(diffs[1] * diffs[3])

# Part 2
def getPathNum (idx=0, pathCount = {}):
    i = idx + 1
    paths = 0
    while i < len(nums) and nums[i] - nums[idx] <= 3:
        if nums[i] in pathCount:
            paths += max(pathCount[nums[i]], 1)
        else:
            paths += max(getPathNum(i, pathCount), 1)
        i += 1
    pathCount[nums[idx]] = paths 
    return paths

print(getPathNum())