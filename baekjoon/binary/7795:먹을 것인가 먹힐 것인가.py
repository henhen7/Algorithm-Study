import sys
input = sys.stdin.readline

# 이분탐색
def binary(target, list):
    start = 0
    end = len(list) -1
    while start <= end:
        mid = (start + end) // 2
        if list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return end

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    count = 0

    for i in a:
        count += binary(i, b) + 1
    print(count)