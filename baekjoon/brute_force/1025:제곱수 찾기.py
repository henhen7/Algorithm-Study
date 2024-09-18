import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = list(input().rstrip() for _ in range(n)) #우측 공백 \n 삭제

ans = 0
chk = False

def check(tmp):
    global ans, chk
    tmp = tmp.replace(' ', '')
    cond = int(tmp) ** (0.5)
    if cond == int(cond):
        if int(tmp) == cond ** 2:
            ans = max(ans, int(tmp))
            chk = True

# 등차수열: a + (n - 1)d (d = 공차)