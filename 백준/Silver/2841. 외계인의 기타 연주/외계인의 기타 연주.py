import sys
input = sys.stdin.readline

n, p = map(int, input().split())
li = [[0] for x in range(7)]
# print(li)
cnt = 0

'''
1. 줄번호마다 스택 생성(7개)
2. 해당 스택에 원소 넣을 때 프랫번호가 크면 In (카운트 +1)
3. 작으면 넣을 원소가 커질때까지 스택에서 out (카운트 +1)
4. 작아지고 나면 넣으면서 카운트 +1
** 같으면 pass
'''

for i in range(n):
    line, plat = map(int, input().split())

    while li[line][-1] > plat:
        li[line].pop()
        cnt += 1

    if li[line][-1] == plat:
        continue

    li[line].append(plat)
    # print(li)
    cnt += 1

print(cnt)
