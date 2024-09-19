import math
# 시간 초과...
n = int(input())
li = list(map(int, input().split()))

def shuffle(card, idx):
    if idx == 0:
        return card
    div_card = card[len(card)-idx:]
    # 올리는 카드의 개수가 두배씩 줄어듬
    return shuffle(div_card, idx//2) + card[:len(card)-idx]

card_li = [i for i in range(1, n + 1)]
# for k1 in range(1, n + 1): # 1024 미만이어야 하니까 단순하게 9로 잡고 했다가 틀림 ..
#     for k2 in range(1, n + 1):
#         if shuffle(shuffle(card_li, 2 ** k1), 2 ** k2) == li:
#             print(k1, k2)

# 여기부터 구글링
m = int(math.log2(n)) # 생각해보니 모든 범위에서 9까지 돌면 안되긴 하다;
ans = []
for k1 in range(1, m + 1):
    for k2 in range(1, m + 1):
        if shuffle(shuffle(card_li, 2 ** k1), 2 ** k2) == li:
            ans.append((k1, k2))
print(*ans[0]) # 중복값이 있을 때 처리..