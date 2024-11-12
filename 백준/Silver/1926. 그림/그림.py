from collections import deque
n, m = map(int, input().split())

# 맵, 방문 리스트 생성
graph = []
visit = []

for _ in range(n):
    graph.append(list(map(int, input().split()))) # 맵

visit = [[False] * m for _ in range(n)] # 방문 리스트

# BFS 함수 생성
def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    visit[x][y] = True # 초기 노드 방문 처리
    count = 1

    # 큐 생성
    while Q:
        (x, y) = Q.popleft()

        # 방향 지정
        dx = [-1, 0, 1, 0]  # 북쪽부터 시계방향
        dy = [0, 1, 0, -1]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m):
                if graph[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    count += 1
                    Q.append((nx, ny))
    return count

ans = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visit[i][j]:
            ans.append(bfs(i, j)) # dfs 함수 돌면서 리스트에 추가

print(len(ans))
if ans:
    print(max(ans))
else:
    print(0)