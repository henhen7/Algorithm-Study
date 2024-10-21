import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a) # b 하려면 a 해야하는거 저장
x = int(input())

visited = [False] * (n + 1)
visited[x] = True
queue = deque([x]) # 선행작업 확인하려고 뒤에서부터 간다

ans = 0
while queue:
    now = queue.popleft()
    for node in graph[now]:
        if not visited[node]:
            queue.append(node)
            visited[node] = True
            ans += 1
print(ans)