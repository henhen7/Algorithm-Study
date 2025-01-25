from collections import deque, defaultdict

max_count = 0
answer_node = defaultdict(int)

def bfs(li, visit):
    global max_count, answer_node
    q = deque()
    q.append((1, 0)) # 현재 노드와 방문 횟수
    visit[1] = True
    
    while q:
        cur_node, cur_count = q.popleft()
        
        if cur_count > max_count:
            max_count = cur_count
        
        if max_count == cur_count:
            answer_node[cur_count] += 1
        
        for i in li[cur_node]:
            if visit[i] == False:
                visit[i] = True
                q.append((i, cur_count + 1))

def solution(n, edge):
    answer = 0
    li = [[] for _ in range(n + 1)]
    visit = [False] * (n + 1)
    
    for a, b in edge:
        li[a].append(b)
        li[b].append(a)
    
    bfs(li, visit)
    answer = answer_node[max_count]
    return answer