def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    
    lost_a = [l for l in lost if l not in reserve]
    reserve_a = [r for r in reserve if r not in lost]
    
    for i in reserve_a:
        pre = i - 1
        next = i + 1
        
        
        if pre in lost_a:
            lost_a.remove(pre)
        elif i + 1 in reserve_a: 
            continue
        elif next in lost_a:
            lost_a.remove(next)
    
    answer = n - len(lost_a)
    return answer