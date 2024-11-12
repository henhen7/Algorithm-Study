'''
n = 1:
0 0 / 0 1 / 1 0 = 3

n = 2: 7
0 0 / 1 0 / 1 0 / 0 1 / 0 1 / 0 0 / 0 0
0 0 / 0 1 / 0 0 / 1 0 / 0 0 / 1 0 / 0 1

n = 3: 17
1 0 / 1 0 / 0 1 / 0 1 / 0 0 / 0 0 / 0 0
0 1 / 0 0 / 1 0 / 0 0 / 1 0 / 0 1 / 0 0

0 0 / 1 0 / 0 1 / 1 0 / 0 1 / 1 0 / 1 0
1 0 / 0 1 / 0 0 / 0 1 / 0 0 / 0 0 / 0 1
    / 0 0       / 0 0             / 0 0

0: n - 1에 사자가 한 마리도 없는 경우
1: n - 1에 사자가 왼쪽에 있는 경우
2: n - 1에 사자가 오른쪽에 있는 경우

1 / 1 / 1
3 / 2 / 2
7 / 5 / 5
17 / 12 / 12
'''

import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n + 1)
for i in range(n + 1) :
    dp[i] = [0, 0, 0]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1


for i in range(2, n + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901

print(sum(dp[n]) % 9901)