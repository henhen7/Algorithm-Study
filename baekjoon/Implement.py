# 24.06.19(수) - 24.06.25(화)
# 유형: 구현
# 문항: 브론즈 1157 / 실버 1316, 2563

# 1157
from collections import defaultdict
n = input()
n = n.upper()

count = defaultdict(int)
for i in n:
    count[i] += 1
li = list(count.values())
M = max(li)
if li.count(M) > 1:
    print("?")
else:
    print(max(count, key=count.get))

# # 1316
# import sys
#
# n = int(sys.stdin.readline())
# word = [sys.stdin.readline().strip() for i in range(n)]
# answer = 0
#
# for i in len(word):
#     print(i)
#
n = int(input())
word = []
answer = 0
for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            new_word = word[j+1:]
            if word[j] in new_word:
                answer -= 1
                break
    answer += 1
print(answer)