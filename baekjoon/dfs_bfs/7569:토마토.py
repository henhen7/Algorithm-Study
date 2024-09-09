import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]
# print(graph)

queue = deque()
# 상, 우, 하, 좌, 위, 아래
dx = [0, 1, 0, -1, 0, 0]
dy = [-1, 0, 1, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

ans = -1

def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = x + dy[i]
            nz = x + dz[i]

            # 익으면 1, 안 익으면 0, 없으면 -1
            if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
                continue

            if graph[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                queue.append((nx, ny, nz))
                graph[nx][ny][nz] = 1
                visited[nx][ny][nz] = True

for a in range(m):
    for b in range(n):
        for c in range(h):
            if graph[a][b][c] == 1 and visited[a][b][c] == 0:
                queue.append((a, b, c))
                visited[a][b][c] = True

bfs()
print(visited)