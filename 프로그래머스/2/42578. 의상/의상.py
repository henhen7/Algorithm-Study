from collections import Counter
import math

def solution(clothes):
    answer = 1
    li = []
    for i in range(len(clothes)):
        li.append(clothes[i][1])
    dict_clothes = Counter(li)
    
    for key, value in dict_clothes.items():
        answer *= (value + 1)
    return answer - 1