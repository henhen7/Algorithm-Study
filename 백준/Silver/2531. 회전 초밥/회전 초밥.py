import sys
from collections import Counter
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
eat_list = Counter()
answer = 0

for i in range(k):
    eat_list[sushi[i]] += 1

if c not in eat_list:
    eat_list[c] = 1
    
answer = max(answer, len(eat_list))

for i in range(1, N):
    eat_list[sushi[i - 1]] -= 1
    if eat_list[sushi[i - 1]] == 0:
        del eat_list[sushi[i - 1]]

    eat_list[sushi[(i + k - 1) % N]] += 1
    if c not in eat_list:
        eat_list[c] = 1

    answer = max(answer, len(eat_list))

print(answer)