from collections import deque

# 스택 수열

n = int(input())

target = [int(input()) for i in range(n)]

stack = deque()

result = []
result_n = []

now = 1 # 스택에 숫자가 1 부터 N까지 오름차순으로 push

for i in range(n):
    while now <= target[i]:
        stack.append(now)
        now += 1 # 4까지 들어가고 나면 now = 5로 세팅
        result.append('+') # 빼줄 숫자가 쌓일 때까지 push하다가
    result.append('-')
    result_n.append(stack.pop()) # 타겟 숫자를 pop

if result_n != target: # 다 돌았는데 결과 리스트가 일치하지 않는 경우
    print('NO')
else:
    print(*result, sep='\n')