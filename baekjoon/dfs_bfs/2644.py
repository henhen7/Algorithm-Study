'''
노드 개수 n
간선 수 m
시작 노드 start_node, 도착 노드 end_node
촌수 count
입력 노드 관계 a, b
'''

n = int(input())
start_node, end_node = map(int, input().split())
m = int(input())

# 인접 리스트 생성
li = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)

for i in li:
    i.sort()

# 방문 리스트 생성
visit = [False] * (n + 1)

ans = -1

# dfs 함수 생성
def dfs(start, end):
    global ans
    count = 0
    stack = [(start, count)]

    while stack:
        (node, count) = stack.pop()
        if node == end:
            ans = count
            return ans
        visit[node] = True
        for i in li[node]:
            if not visit[i]:
                stack.append((i, count + 1))
                # print(stack)

dfs(start_node, end_node)
print(ans)

# n = int(input())
# start_node, end_node = map(int, input().split())
# m = int(input())
#
# # 인접 리스트 생성
# li = [[] for _ in range(n + 1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     li[a].append(b)
#     li[b].append(a)
#
# for i in li:
#     i.sort()
#
# # 방문 리스트 생성
# visit = [False] * (n + 1)
# ans = -1
# count = 0
#
# # dfs 함수 생성
# def dfs(start, end):
#     global count
#     global ans
#     if start == end:
#         ans = count
#         return ans
#     visit[start] = True
#     count += 1
#
#     for i in li[start]:
#         if not visit[i]:
#             dfs(i, end)
#
# dfs(start_node, end_node)
# print(ans)


# # dfs 함수 생성
# def dfs(start, end):
#     global count
#     global ans
#     if start == end:
#         ans = count
#         return ans
#     visit[start] = True
#
#     for i in li[start]:
#         if not visit[i]:
#             count += 1
#             dfs(i, end)
#     count -= 1