from collections import deque

t = int(input())

def bfs(graph):
    def check_all(graph): 
        first = graph[0][0]
        for i in range(3):
            for j in range(3):
                if graph[i][j] != first:
                    return False
        return True

    def graph_to_string(graph):
        return ''.join(''.join(row) for row in graph)

    start = graph_to_string(graph)
    visited = set([start])
    queue = deque([(graph, 0)])

    while queue:
        current_graph, count = queue.popleft()

        if check_all(current_graph):
            return count

        for i in range(3):
            # 행 뒤집기
            # 2차원 리스트 복제
            temp = [row[:] for row in current_graph]
            for j in range(3):
                if current_graph[i][j] == "H":
                    temp[i][j] = "T"
                else:
                    temp[i][j] = "H"
            new_graph_str = graph_to_string(temp)
            if new_graph_str not in visited:
                visited.add(new_graph_str)
                queue.append((temp, count + 1))

            # 열 뒤집기
            temp = [row[:] for row in current_graph]
            for j in range(3):
                if current_graph[j][i] == "H":
                    temp[j][i] = "T"
                else:
                    temp[j][i] = "H"
            new_graph_str = graph_to_string(temp)
            if new_graph_str not in visited:
                visited.add(new_graph_str)
                queue.append((temp, count + 1))

        # 왼쪽 위 -> 오른쪽 아래 대각선 뒤집기
        temp = [row[:] for row in current_graph]
        for i in range(3):
            if current_graph[i][i] == "H":
                temp[i][i] = "T"
            else:
                temp[i][i] = "H"
        new_graph_str = graph_to_string(temp)
        if new_graph_str not in visited:
            visited.add(new_graph_str)
            queue.append((temp, count + 1))

        # 오른쪽 위 -> 왼쪽 아래 대각선 뒤집기
        temp = [row[:] for row in current_graph]
        for i in range(3):
            if current_graph[i][2 - i] == "H":
                temp[i][2 - i] = "T"
            else:
                temp[i][2 - i] = "H"
        new_graph_str = graph_to_string(temp)
        if new_graph_str not in visited:
            visited.add(new_graph_str)
            queue.append((temp, count + 1))

    return -1

for _ in range(t):
    graph = [list(input().split()) for _ in range(3)]
    print(bfs(graph))
