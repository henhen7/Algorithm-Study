def solution(n, sol_list):
    left = 0
    right = n - 1
    target = float('inf')
    answer = [0, 0]

    while left < right:
        cur_sum = sol_list[left] + sol_list[right]

        #절댓값 비교
        if abs(cur_sum) < abs(target):
            target = cur_sum
            answer = [sol_list[left], sol_list[right]]

        if cur_sum > 0:
            right -= 1
        elif cur_sum < 0:
            left += 1
        else:
            return sol_list[left], sol_list[right]

    return answer[0], answer[1]

n = int(input())
sol_list = list(map(int, input().split()))

sol1, sol2 = solution(n, sol_list)
print(sol1, sol2)