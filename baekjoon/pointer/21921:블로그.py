import sys
input = sys.stdin.readline

n, x = map(int, input().split())
li = list(map(int, input().split()))

sum = 0
cnt = 1

left = 0
right = x - 1
for i in range(x):
    sum += li[i]
ans = sum

while right < n - 1:
    # 포인터를 하나씩 이동하면서 확인
    sum -= li[left]
    left += 1
    right += 1
    sum += li[right]
    if ans < sum:
        ans = sum
        cnt = 1
    elif ans == sum:
        cnt += 1

if ans == 0:
    print("SAD")
else:
    print(ans)
    print(cnt)