import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())

v = list(map(int, input().split()))
def function(number, cnt):
    if number < 0 or number > m:
        return
    if cnt == n:
        if number not in ans:
            ans.append(number)
        return
    a = number + v[cnt]
    function(a, cnt + 1)
    b = number - v[cnt]
    function(b, cnt + 1)

ans = []
function(s,0)
print(max(ans) if ans else -1)