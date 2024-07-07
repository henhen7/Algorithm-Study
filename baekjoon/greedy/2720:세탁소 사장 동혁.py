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