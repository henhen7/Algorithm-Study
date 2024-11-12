def solve(diffs, times, level, limit):
    total_time = 0
    total_time += times[0]
    
    for i in range(1, len(diffs)): # 두번째 문제부터 풀어야 함
        time_cur = times[i]
        time_prev = times[i - 1]
        diff = diffs[i]
        
        if diff <= level:
            total_time += time_cur
        else:
            mistake = diff - level
            total_time += mistake * (time_cur + time_prev) + time_cur
        if total_time > limit:
            return False
    return True

def solution(diffs, times, limit):
    left = 1
    right = 100001
    
    while left < right:
        mid = (left + right) // 2
        if solve(diffs, times, mid, limit):
            right = mid
        else:
            left = mid + 1
    
    answer = left
    return answer