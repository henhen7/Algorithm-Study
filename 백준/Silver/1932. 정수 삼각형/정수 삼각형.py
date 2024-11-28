import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

'''
1 = 초기
2 -> 1 = 0 -> 0, 1 -> 0
3 -> 2 = 0 -> 0, 1 -> 0 1, 2 -> 1
4 -> 3 = 0 -> 0, 1 -> 0 1, 2 -> 1 2, 3 -> 2
'''

dp = [[0] * n for _ in range(n)]
dp[0][0] = li[0][0]

for i in range(1, n):
    for j in range(0, i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + li[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + li[i][j]

print(max(dp[n - 1]))