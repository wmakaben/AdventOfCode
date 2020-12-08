file = open("input/d08.txt", 'r')

code = [line.rstrip().split(" ") for line in file]

accumulator = 0
visited = set()
i = 0

while i not in visited:
    op = code[i][0]
    arg = int(code[i][1])
    visited.add(i)
    if op == "acc":
        accumulator += arg
        i += 1
    elif op == "jmp":
        i += arg
    elif op == "nop":
        i += 1

print(accumulator)

