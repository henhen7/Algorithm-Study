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
for k1 in range(1, n + 1):
    for k2 in range(1, n + 1):
        if shuffle(shuffle(card_li, 2 ** k1), 2 ** k2) == li:
            print(k1, k2)
