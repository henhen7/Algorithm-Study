# 24.6.12 (수) - 24.06.18(화)
# 유형: 그리디 알고리즘
# 문항: 브론즈 2720 / 실버 1541, 1026

#1026
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
a.sort()
b.sort(reverse=True)

for i in range(n):
    ans += a[i]*b[i]
print(ans)