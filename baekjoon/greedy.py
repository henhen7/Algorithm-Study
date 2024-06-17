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

# 1541
# 최소값 되려면 다음 - 부호 나오기 전 - 부호 식을 다 묶어야 함
# - 단위로 쪼개기
li = input().split("-")
tot = 0

# 쪼개진 식 중 + 단위로 숫자 다시 쪼개기(2차원 배열)
for i in range(len(li)):
    li[i] = li[i].split("+")

# 첫 번째 - 이전 모든 값 다 더해서 초기값으로 지정
tot = sum(map(int, li[0]))

for i in range(1, len(li)):
    minus = 0
    for j in range(len(li[i])):
        minus += int(li[i][j])

    tot -= minus

print(tot)

# 2720
n = int(input())
coins = [25, 10, 5, 1]
ans = []

for _ in range(n):
    c = int(input())
    for coin in coins:
        ans.append(c // coin)
        c = c % coin

for i in range(0, len(ans), 4):
    print(*ans[i:i+4])