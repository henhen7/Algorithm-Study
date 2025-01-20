from collections import Counter

def solution(participant, completion):
    answer = 0
    union_li = participant + completion
    union_dict = Counter(union_li)
    # print(union_dict)
    for key, value in union_dict.items():
        if value % 2 == 1:
            answer = key
    return answer