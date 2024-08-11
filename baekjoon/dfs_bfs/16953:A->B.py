from collections import deque
a, b = map(int, input().split())

def AtoB(start, end):
    global ans
    count = 0
    Q = deque([(start, count)])
    # 방문 리스트 탐색 시간이 너무 길어져서
    # pypy3으로 겨우 통과하는 문제 발생.. set으로 자료구조 변경
    visit = set([start])

    while Q:
        (start, count) = Q.popleft()

        if start == end:
            return count + 1

        # 곱하기
        # end보다 작을 때 조건 추가(없을 시 무한루프로 -1 출력 불가능)
        if (start * 2) <= end not in visit:
            visit.add(start * 2)
            Q.append(((start * 2), count + 1))
            #print(Q)

        # 마지막 자릿수 1 더하기
        # end보다 작을 때 조건 추가(없을 시 무한루프로 -1 출력 불가능)
        if (start * 10 + 1) <= end not in visit:
            visit.add(start * 10 + 1)
            Q.append(((start * 10 + 1), count + 1))
            #print(Q)
    return -1

ans = AtoB(a, b)
print(ans)