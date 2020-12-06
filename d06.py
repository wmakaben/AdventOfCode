file = open("input/d06.txt", 'r')

count = 0
group = 0
questions = {}

def getQuestionCount (questionMap, groupCount):
    c = 0
    for qCount in questionMap.values():
        if qCount == group:
            c += 1
    return c

for line in file:
    line = line.rstrip()
    if line == "":
        count += getQuestionCount(questions, group)
        questions.clear()
        group = 0
    else:
        group += 1
        for q in line:
            if q not in questions:
                questions[q] = 0
            questions[q] += 1

count += getQuestionCount(questions, group)

print(count)