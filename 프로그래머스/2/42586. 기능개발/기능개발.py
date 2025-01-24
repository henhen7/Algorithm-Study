import math

def solution(progresses, speeds):
    answer = []
    works_time = []
    for i in range(len(progresses)):
        works_time.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    while works_time:
        x = works_time.pop(0)
        result = 1
        while len(works_time) >= 1 and x >= works_time[0]:
            works_time.pop(0)
            result += 1
        answer.append(result)
    return answer