import sys
input = sys.stdin.readline
li = []

n = int(input())
for _ in range(n):
    li.append(list(map(int, input().split())))

# 종료 시간 기준으로 정렬, 일치 시 시작 시간 순서
li.sort(key=lambda x:(x[1], x[0]))
#print(li)

ans = 0
lastEndTime = 0

for i in range(len(li)):
    if li[i][0] >= lastEndTime:
        ans += 1
        lastEndTime = li[i][1]

print(ans)