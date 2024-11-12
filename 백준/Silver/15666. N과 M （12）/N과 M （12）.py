n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
# 방문 체크: 중복은 불가능하나 같은 수가 2개 이상 들어있다면
# [n,n] 출력이 필요함.. 리스트 단에서 중복 제거가 불가능함
def function(start):
    if len(ans) == m:
        print(*ans)
        return
    chk = 0 # 중복 수열 제거
    for i in range(start, n):
        if chk != num[i]:
            ans.append(num[i])
            chk = num[i] # 포인터를 이동시킴
            function(i) # 다음 호출에서 현재 인덱스부터 시작
            ans.pop()

ans = []
function(0)