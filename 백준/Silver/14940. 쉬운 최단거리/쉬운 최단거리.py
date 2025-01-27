import sys
from collections import deque
input = sys.stdin.readline

'''
1. 아이디어: BFS
2. 자료구조:
n, m: 세로, 가로(2 ~ 1000)
graph = [] (0: 갈 수 없음, 1: 갈 수 있음, 2: 목표 지점)
visited = [False]
deque = ((x, y, 거리) -> 2인 목표 지점을 기준으로 전부 다 dfs 돌리면?
'''
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
answer = [[-1] * m for _ in range(n)]

def bfs(graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue = deque([(i, j, 0)])
                visited[i][j] = True
                answer[i][j] = 0
                break

    while queue:
        x, y, cnt = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] != 0:
                    visited[nx][ny] = True
                    answer[nx][ny] = cnt + 1
                    queue.append((nx, ny, cnt + 1))

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                answer[i][j] = 0

    return answer

result = bfs(graph)
for row in result:
    print(" ".join(map(str, row)))