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


'''
1 3 6 10 15 ...
1 4 10 20 35 ...

n = 1 -> 1
n = 2 -> 2
n = 3 -> 3
n = 4 -> 1
n = 5 -> 2
n = 6 -> 3
n = 7 -> 4
n = 8 -> 2
n = 9 -> 3

a = 1 i = 2
dp[2] = min(dp[2], 1 + dp[1])
dp[2] = 2

dp[3] = min(dp[3], 1 + dp[2])
dp[3] = 3


a = 4 i = 2
break

a = 4 i = 4
dp[4] = min(dp[4], 1 + dp[0])
dp[4] = 1

'''