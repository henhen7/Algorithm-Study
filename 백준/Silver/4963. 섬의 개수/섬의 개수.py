import sys
input = sys.stdin.readline
def dfs(x, y, w, h, graph, visited):
    # directions: 위부터 대각선 칸을 포함하여 시계방향으로 작성
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop() # current: 현재 방문한 칸
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy # 반복문을 돌며 인근 탐색
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and graph[ny][nx] == 1:
                visited[ny][nx] = True # 섬으로 표시되어 있고 방문하지 않은 경우, 방문 처리하고 해당 칸을 스택에 추가
                stack.append((nx, ny))


def count(w, h, graph):
    visited = [[False] * w for _ in range(h)]
    count = 0

    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1 and not visited[y][x]:
                visited[y][x] = True
                dfs(x, y, w, h, graph, visited)
                count += 1
    return count

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
         break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    print(count(w, h, graph))