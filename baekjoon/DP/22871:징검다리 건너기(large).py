# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# stone = [0] + list(map(int, input().split()))
# s, e, r = 1, (n - 1) * (1 + abs(stone[n] - stone[1])), 0
#
# while s <= e:
#     m = (s + e) // 2
#     flag = 0
#     stack = [1]
#     visited = [False] * (n + 1)
#     visited[1] = True
#
#     while stack:
#         k = stack.pop()
#
#         if k == n:
#             flag = 1
#             break
#
#         for i in range(k + 1, n + 1):
#             p = (i - k) * (1 + abs(stone[i] - stone[k]))
#             if p <= m and not visited[i]:
#                 stack.append(i)
#                 visited[i] = True
#
#     if flag:
#         e = m - 1
#         r = m
#     else:
#         s = m + 1
#
# print(r)


# DP
INF = 99999999
n = int(input())
A = list(map(int, input().split()))
# dp[i]는 i까지 가는데 드는 최소 힘
dp = [0] + [INF] * (n - 1)

for i in range(1, n):
    for j in range(0, i):
        power = max((i - j) * (1 + abs(A[i] - A[j])), dp[j])
        dp[i] = min(dp[i], power)

print(dp[-1])