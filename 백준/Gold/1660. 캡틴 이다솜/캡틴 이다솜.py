import sys
input = sys.stdin.readline

N = int(input())
li = []
a = 0
idx = 1
while a < N:
    a += (idx * (idx + 1)) // 2
    li.append(a)
    idx += 1
dp = [999999] * (N + 1)
dp[0] = 0
dp[1] = 1
for i in range(2, N + 1):
    for a in li:
        if a > i: break
        dp[i] = min(dp[i], 1 + dp[i - a])
print(dp[N])