import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
answer = 0

def bfs(n, graph, rain):
    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            # 안전 지역이고 방문하지 않았을 때 탐색
            if graph[i][j] > rain and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True

                while queue:
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            if graph[nx][ny] > rain:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                cnt += 1
    return cnt

for rain in range(101):
    answer = max(answer, bfs(n, graph, rain))

print(answer)