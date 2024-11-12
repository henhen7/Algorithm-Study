import sys
sys.setrecursionlimit(10**7)  # 재귀함수 깊이 설정

input = sys.stdin.readline
t = int(input())

def dfs(x, y):
    dx = [-1, 0, 1, 0] # 북쪽부터 시계방향
    dy = [0, 1, 0, -1]
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 1 and not visit[x][y]:
        visit[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True

    return False


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visit = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                cnt += 1
    print(cnt)