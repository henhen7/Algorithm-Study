import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = sorted(list(map(int, input().split())))

# 자른 나무 길이
def cal_wood(height):
    length = 0
    for i in range(len(tree)):
        if tree[i] >= height:
            length += (tree[i]-height)
    return length

# 이분탐색
def binary(tree, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        length = cal_wood(mid)
        if length < target:
            end = mid - 1
        else:
            start = mid + 1
    return end

print(binary(tree, M, 0, tree[-1]))