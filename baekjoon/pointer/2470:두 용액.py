import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.sort()

left = 0
right = n - 1
ans = []
sum = float('inf')

if n == 2:
    print(*sorted(li))
else:
    while left < right:
        sum_now = li[left] + li[right]
        # 값이 0에 가까운 경우 정답 갱신
        if abs(sum_now) < abs(sum):
            sum = sum_now
            ans = [li[left], li[right]]
        if sum_now < 0:
            left += 1
        else:
            right -= 1
print(*sorted(ans))

# -5 -4 -3 -2 -1 0 2 4 5
#
# -5 5 -> 0
# -5 4 -> 1
# -5 2 -> -3
# -4 2 -> -2
# -2 2 -> 0
# -1 2 -> 1
# -1 0 -> -1
# 0 0 : 같은 위치에 포인터(종료)