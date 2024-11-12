import sys
input = sys.stdin.readline

# n = int(input())
# li = list(map(int, input().split()))
# m = int(input())
# ans = 0
#
# li.sort()
#
# print(li)
#
# for i in range(len(li)):
#     if li[i] <= m:
#         m -= li[i]
#         ans = li[i]
#     else:
#         ans = m // (len(li) - i)
#
# print(ans)

n = int(input())
li = list(map(int, input().split()))
m = int(input())

start = 0
end = max(li)  # 이진 탐색 범위는 0부터 최대 예산 요청액까지
ans = 0

while start <= end:
    mid = (start + end) // 2  # 상한액을 중간값으로 설정
    total = 0

    for i in li:
        if i > mid:
            total += mid
        else:
            total += i

    if total <= m:  # 총 예산 m보다 작거나 같은 경우
        ans = mid
        start = mid + 1  # 상한액을 더 높여서 시도
    else:  # 총 예산 m을 초과하는 경우
        end = mid - 1  # 상한액을 낮춰서 시도

print(ans)