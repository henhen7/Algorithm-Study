# 입력: 첫째 줄에 정수 N 입력 (0<=N<=23)
# 출력: 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력

n = int(input())

ans = 0
for i in range(n + 1): #시
    for j in range(60): #분
        for k in range(60): #초
            if '3' in str(i) + str(j) + str(k): #완전 탐색
                ans += 1
print(ans)