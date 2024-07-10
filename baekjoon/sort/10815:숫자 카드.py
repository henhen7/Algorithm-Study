# 시간초과 미쳣나
# import sys
# input = sys.stdin.readline
# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))
# ans = [0] * m
#
# for i in range(m):
#     if b[i] in a:
#         ans[i] = 1
# print(*ans)

import sys
input = sys.stdin.readline
n = int(input())
# a를 set으로 처리: set은 중복을 허용하지 않으므로 시간 단축(n 개수가 많다.)
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ans = [0] * m

for i in range(m):
    if b[i] in a:
        ans[i] = 1
print(*ans)