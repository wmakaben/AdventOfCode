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

def getBusOffsetMap (buses):
    offsetMap = {}
    for i in range(0, len(buses)):
        if buses[i] == 'x':
            continue
        offsetMap[int(buses[i])] = i
    return offsetMap

def isThatTime (time, buses, offsets):
    for b in buses:
        if (time + offsets[b]) % b != 0:
            return False
    return True

def partTwo(buses):
    offsets = getBusOffsetMap(buses)
    busIds = [int(id) for id in buses if id != 'x']

    maxBusTime = max(busIds)
    offset = buses.index(str(maxBusTime))
    print(maxBusTime, offset)

    timeMultiplier = 1
    # timeMultiplier = 17001991
    time = (maxBusTime * timeMultiplier) - offset
    while not isThatTime(time, busIds, offsets):
        # print(timeMultiplier, time)
        timeMultiplier += 1
        time = (maxBusTime * timeMultiplier) - offset
    print(time)

# partOne(t, b)
partTwo(b)