file = open("input/d08.txt", 'r')

code = [line.rstrip().split(" ") for line in file]

# accumulator = 0
# visited = set()
# i = 0

# while i not in visited:
#     op = code[i][0]
#     arg = int(code[i][1])
#     visited.add(i)
#     if op == "acc":
#         accumulator += arg
#         i += 1
#     elif op == "jmp":
#         i += arg
#     elif op == "nop":
#         i += 1

# print(accumulator)

def getAccumulator (idx = 0, visited = set(), switch = True):
    if idx >= len(code):
        return 0

    # print(" " * len(visited), code[idx])
    if idx in visited:
        return None
    
    accumulator = 0
    visited.add(idx)
    op = code[idx][0]
    arg = int(code[idx][1])

    if op == "acc":
        accumulator += arg
        idx += 1
    elif op == "jmp":
        tmpAcc = None
        if switch:
            tmpAcc = getAccumulator(idx + 1, set(visited), False)
        if tmpAcc is None:
            idx += arg
        else:
            return accumulator + tmpAcc
    elif op == "nop":
        tmpAcc = None
        if switch:
            tmpAcc = getAccumulator(idx + arg, set(visited), False)
        if tmpAcc is None:
            idx += 1
        else:
            return accumulator + tmpAcc

    nextAcc = getAccumulator(idx, visited, switch)
    if nextAcc is None:
        return None
    return accumulator + nextAcc

print(getAccumulator())