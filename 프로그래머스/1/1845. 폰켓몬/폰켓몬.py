from collections import Counter
def solution(nums):
    answer = 0
    dict_nums = Counter(nums)
    li = list(dict_nums.keys())
    if len(li) >= len(nums) / 2:
        answer = len(nums) / 2
    else : 
        answer = len(li)
    return answer