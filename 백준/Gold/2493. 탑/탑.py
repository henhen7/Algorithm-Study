def solution(n, tower_list):
    result = [0] * n
    tower_stack = []
    for i in range(n):
        while tower_stack and tower_stack[-1][1] < tower_list[i]:
                tower_stack.pop()
        if tower_stack:
            result[i] = tower_stack[-1][0] + 1
        tower_stack.append((i, tower_list[i]))
    return result

k = int(input())
tower = list(map(int, input().split()))

answer = solution(k, tower)
print(' '.join(map(str, answer)))