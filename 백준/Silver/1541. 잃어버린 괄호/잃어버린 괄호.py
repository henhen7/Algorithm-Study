# 최소값 되려면 다음 - 부호 나오기 전 - 부호 식을 다 묶어야 함
# - 단위로 쪼개기
li = input().split("-")
tot = 0

# 쪼개진 식 중 + 단위로 숫자 다시 쪼개기(2차원 배열)
for i in range(len(li)):
    li[i] = li[i].split("+")

# 첫 번째 - 이전 모든 값 다 더해서 초기값으로 지정
tot = sum(map(int, li[0]))

for i in range(1, len(li)):
    minus = 0
    for j in range(len(li[i])):
        minus += int(li[i][j])

    tot -= minus

print(tot)