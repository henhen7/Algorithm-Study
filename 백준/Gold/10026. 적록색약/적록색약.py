import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(input().strip()) for _ in range(N)]
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def bfs(style):
    visited = [[False] * N for _ in range(N)]
    cnt_normal = 0
    cnt_weak = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            if style == 'weak':
                                if graph[i][j] in ['R', 'G'] and graph[nx][ny] in ['R', 'G']:
                                    visited[nx][ny] = True
                                    queue.append((nx, ny))
                                elif graph[i][j] == 'B' and graph[nx][ny] == 'B':
                                    visited[nx][ny] = True
                                    queue.append((nx, ny))
                            else:
                                if graph[i][j] == graph[nx][ny]:
                                    visited[nx][ny] = True
                                    queue.append((nx, ny))
                if style == 'weak': cnt_weak += 1
                else: cnt_normal += 1
    if style == 'weak': return cnt_weak
    else: return cnt_normal

print(bfs('normal'), bfs('weak'))