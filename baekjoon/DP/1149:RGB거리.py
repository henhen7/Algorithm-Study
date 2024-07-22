import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))


for i in range(1, n): # 1회부터 시작
    # 현재 빨간색을 선택한 경우, 이전 회차(ex. 첫 번째 주어진 집)에서 빨간색을 제외한
    # 파란색, 초록색 중 최저 비용을 선택한다. 다른 색상도 마찬가지로 진행한다.
    li[i][0] = min(li[i - 1][1], li[i - 1][2]) + li[i][0]
    li[i][1] = min(li[i - 1][0], li[i - 1][2]) + li[i][1]
    li[i][2] = min(li[i - 1][0], li[i - 1][1]) + li[i][2]

print(min(li[n - 1][0], li[n - 1][1], li[n - 1][2]))