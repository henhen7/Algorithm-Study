n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [0] * n
# 방문 체크: 중복은 불가능하나 같은 수가 2개 이상 들어있다면
# [n,n] 출력이 필요함.. 리스트 단에서 중복 제거가 불가능함
def function():
    chk = 0
    for i in range(n):
        if chk != num[i] and visited[i] == 0:
            ans.append(num[i])
            visited[i] = 1
            chk = num[i] # 포인터를 이동시킴
            function() # DFS로 계속 탐색
            # 재귀호출 후 이전 상태로 돌아감(백트래킹)
            # 새로운 조합 탐색
            ans.pop()
            visited[i] = 0
    if len(ans) == m:
        print(*ans)
        return


ans = []
function()