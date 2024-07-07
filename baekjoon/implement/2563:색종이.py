# 색종이의 수
n = int(input())

# 색종이 위치 입력(좌하단 꼭짓점의 좌표)
li = [list(map(int, input().split())) for _ in range(n)]

# 입력받은 색종이의 위치를 스택에 넣고 꺼내면서 방문 처리
# 1 * 1 칸의 넓이는 1이다

# 방문 리스트 생성
graph = []
for _ in range(101):
    graph.append([0] * 101)

# 스택을 돌면서 방문 처리
while li:
    x, y = li.pop()
    for i in range(10):
        for j in range(10):
            graph[x + i][y + j] = 1

# # 출력 확인하기
# for i in range(100):
#     for j in range(100):
#         print(graph[i][j], end = '')
#     print()

ans = 0
for i in graph:
    ans += sum(i)
print(ans)