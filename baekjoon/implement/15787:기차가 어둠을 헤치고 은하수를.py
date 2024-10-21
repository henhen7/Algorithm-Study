from collections import deque
n, m = map(int, input().split())
# 0 : 빈자리, 1: 탑승
trains = [deque([0] * 20) for _ in range(n)]
patterns = []
answer = 0
for _ in range(m):
    command = list(map(int, input().split()))
    # 승차
    if command[0] == 1:
        i, j = command[1] - 1, command[2] - 1
        if trains[i][j] == 0:
            trains[i][j] = 1
    # 하차
    elif command[0] == 2:
        i, j = command[1] - 1, command[2] - 1
        if trains[i][j] == 1:
            trains[i][j] = 0
    # 왼쪽 이동
    elif command[0] == 3:
        i = command[1] - 1
        trains[i].appendleft(0)
        trains[i].pop()
    # 오른쪽 이동
    elif command[0] == 4:
        i = command[1] - 1
        trains[i].append(0)
        trains[i].popleft()

for i in range(n):
    # print(trains[i])
    if trains[i] not in patterns:
        answer += 1
        patterns.append(trains[i])
    else:
        continue
print(answer)
