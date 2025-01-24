from collections import deque
def solution(s):
    answer = True
    left = 0
    right = 0
    li = deque()
    for i in s:
        li.append(i)
    
    while li:
        x = li.popleft()
        if x == "(":
            left += 1
        else: right += 1
        if right > left:
            return False
    if right != left:
        return False
        
    return True