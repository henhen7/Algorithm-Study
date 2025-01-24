from collections import deque

def solution(priorities, location):
    queue = deque()
    for i in range(len(priorities)):
        queue.append((priorities[i], i))
    answer = 0
    while queue:
        x = queue.popleft()
        if len(queue) > 1 and x[0] < max(i[0] for i in queue):
            queue.append(x)
        else:
            answer += 1
            if x[1] == location:
                return answer
    return answer