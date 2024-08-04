import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
li = list(map(int, input().split()))

def light_all(length, place, light):
    # 시작 위치
    current = 0

    for i in place:
        if i - light > current:
            # 현재 가로등이 비출 수 없는 구간이 생김
            return False
        current = i + light
        if current >= length:
            # 굴다리의 끝까지 밝히면 True 반환
            return True
    # 마지막 가로등으로 굴다리 끝을 밝힐 수 있는지 확인
    return current >= length


def binary(length, place):
    # 이분탐색 범위 설정
    start = 1
    end = length

    while start <= end:
        mid = (start + end) // 2
        if light_all(length, place, mid):
            start = mid - 1
        else:
            end = mid + 1
    return end


# 최소 높이 계산
print(binary(n, li))


def can_light_all(length, lamps, height):
    # 시작 위치
    current_end = 0

    for lamp in lamps:
        if lamp - height > current_end:
            # 현재 가로등이 비출 수 없는 구간이 생김
            return False
        current_end = lamp + height
        if current_end >= length:
            # 굴다리의 끝까지 밝히면 True 반환
            return True

    # 마지막 가로등으로 굴다리 끝을 밝힐 수 있는지 확인
    return current_end >= length


def find_min_height(length, lamps):
    # 이분탐색 범위 설정
    low, high = 1, length
    result = length

    while low <= high:
        mid = (low + high) // 2
        if can_light_all(length, lamps, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


# 입력 받기
n = int(input().strip())
m = int(input().strip())
lamps = list(map(int, input().strip().split()))

# 최소 높이 계산
min_height = find_min_height(n, lamps)
print(min_height)