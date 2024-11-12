import sys
input = sys.stdin.readline

n, m = map(int, input().split())

list = [[0] * (n + 1)] # 편의를 위해 (1,1)부터 연산

for _ in range(n):
    nums = [0] + [int(x) for x in input().split()]
    list.append(nums)
    # print(list)

# 행 sum
for i in range(1, n + 1):
    for j in range(1, n):
        list[i][j + 1] += list[i][j]

# 열 sum
for j in range(1, n + 1):
    for i in range(1, n):
        list[i + 1][j] += list[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(list[x2][y2] - list[x1 - 1][y2] - list[x2][y1 - 1] + list[x1 - 1][y1 - 1])
