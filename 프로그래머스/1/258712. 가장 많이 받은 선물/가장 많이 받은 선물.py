def solution(friends, gifts):
    answer = [0] * len(friends)
    table = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    gift_list = [0] * len(friends)
    
    # 선물 배열 지정
    for gift in gifts:
        give, take = gift.split(" ")
        # 계산 편의를 위해 friends 배열의 인덱스 번호로 지정
        give_idx = friends.index(give)
        take_idx = friends.index(take)
        # 이전 달 선물 지수 계산
        gift_list[give_idx] += 1
        gift_list[take_idx] -= 1
        # n*n 선물 배열 생성
        table[give_idx][take_idx] += 1
    # print(table)
    # print(gift_list)
    
    # 다음 달 선물 계산
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if table[i][j] > table[j][i]:
                answer[i] += 1
            elif table[i][j] < table[j][i]:
                answer[j] += 1
            else: # 선물 배열이 같은 경우
                if gift_list[i] > gift_list[j]:
                    answer[i] += 1
                elif gift_list[i] < gift_list[j]:
                    answer[j] += 1
    return max(answer)