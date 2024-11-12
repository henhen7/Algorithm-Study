import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
li = list(map(int, input().split()))
li.sort(reverse=True)
cnt = 0

for i in range(len(li)):
    if m <= li[i]:
        continue
    if m > li[i]:
        for j in range(i+1, len(li)):
            if li[i] + li[j] == m:
                cnt += 1

print(cnt)