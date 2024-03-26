# 위치 입력
input = input()

# 행, 열 지정
row = int(input[1])
column = int(ord(input[0]) - 97 + 1) #ord('a') = 97

# 이동 범위 리스트 생성
steps = [(1,2), (-1,2), (1,-2), (-1,-2), (2,1), (-2,1), (2,-1), (-2,-1)]
ans = 0

# 지정된 위치에서 이동 가능한 횟수 세기
for i in steps:
    nr = row + i[0]
    nc = column + i[1]
    # 이동 범위를 주어진 배열 안으로 지정
    if nr >= 1 and nr <= 8 and nc >= 1 and nc <= 8:
        ans += 1

print(ans)