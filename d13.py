import math

file = open("input/d13.txt", 'r')

t = int(file.readline().rstrip())
b = file.readline().rstrip().split(',')

def partOne(time, buses):
    busSet = set(buses)
    busSet.remove('x')
    nextBus = -1
    minWait = -1

    for bus in busSet:
        busId = int(bus)
        wait = math.ceil(time / busId) * busId - time
        if minWait < 0 or wait < minWait:
            minWait = wait
            nextBus = busId
    print("Bus: ", nextBus, ", Wait: ", minWait, ", Answer: ", nextBus * minWait)

partOne(t, b)