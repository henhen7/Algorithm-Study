import sys
input = sys.stdin.readline

k, n = map(int, input().split())
li = [int(input()) for _ in range(k)]
li.sort()

# 랜선 개수 카운트
def count_line(list, length):
    count = 0
    for i in list:
        count += i // length
        # 랜선에서 length만큼 잘라낸 몫을 전부 더해서 카운트에 연산
    return count

# 이분탐색
def binary(list, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        count = count_line(list, mid)
        if count < target:
            end = mid - 1
        else:
            start = mid + 1
    return end

print(binary(li, n, 1, li[-1]))