n, m, s = map(int, input().split())
li = [[] for _ in range(m + 1)]

# 인접 리스트 생성
for _ in range(m):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)

# 각 리스트의 원소(정점)을 오름차순으로 정렬
for i in li:
    i.sort()

## DFS
# 방문 리스트 생성
visit_dfs = [False] * (n + 1)

dfs_ans = []
# 재귀함수 생성
def dfs(node):
    visit_dfs[node] = True
    dfs_ans.append(node)

    for i in li[node]:
        if not visit_dfs[i]:
            dfs(i)

dfs(s)
print(*dfs_ans)

## BFS
from collections import deque
# 방문 리스트 생성
visit_bfs = [False] * (n + 1)
bfs_ans = []

# 큐 생성
def bfs(node):
    Q = deque([node]) #시작 노드 추가
    while Q:
        node = Q.popleft()

        if not visit_bfs[node]:
            visit_bfs[node] = True
            for i in li[node]:
                Q.append(i)
            bfs_ans.append(node)
bfs(s)
print(*bfs_ans)

# 방문 처리 리스트 생성
# visit = [False] * (n + 1)
# stack = [s]
# dfs = []
#
# # DFS 스택 생성
# while stack:
#     node = stack.pop() # 방문 노드 처리
#     if not visit[node]:
#         visit[node] = True
#         # 해당 노드에 연결된 노드의 리스트를 역순으로 순회하며 스택에 쌓음
#         # 스택처리 시 큰 노드를 먼저 쌓고 작은 노드를 먼저 꺼내기 위함
#         for i in reversed(li[node]):
#             stack.append(i)
#         dfs.append(node)
