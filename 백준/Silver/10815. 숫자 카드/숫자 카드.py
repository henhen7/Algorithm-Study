import sys
input = sys.stdin.readline
n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ans = [0] * m

for i in range(m):
    if b[i] in a:
        ans[i] = 1
print(*ans)