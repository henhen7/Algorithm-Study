# 문제 조건
# 배열의 크기 n, 숫자가 더해지는 횟수 m, 같은 수가 연속으로 더해질 수 있는 횟수 k가 주어질 때, 큰 수의 법칙에 따라 가장 큰 결과를 나타낸다.

# map(int, input().split()): 복수의 자료형 요소들(split()으로 리스트로 변형된 입력값)을 특정 함수(Int)에 대응
n, m, k = map(int, input('n, m, k에 해당하는 수를 공백으로 입력하여 주세요.').split())
data = list(map(int, input('n개의 수를 공백으로 입력하여 주세요.').split()))

data.sort()

# 가장 큰 수 k회 + 두 번째로 큰 수 1회 더하기 위하여 변수 지정
first = data[n-1]
second = data[n-2]

ans = 0

while True:
    for i in range(k):
        if m == 0: # m이 0이라면 반복문 탈출
            break
        ans += first
        m = m - 1 # 카운트 감소

    if m == 0:
        break
    ans += second
    m -= 1

print(ans)