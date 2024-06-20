# 24.06.19(수) - 24.06.25(화)
# 유형: 구현
# 문항: 브론즈 1157 / 실버 1316, 2563

# 1157
# from collections import defaultdict
# n = input()
#
# count = defaultdict(int)
# for i in n:
#     count[i] += 1
# li = list(count.values())
# M = max(li)
# if li.count(M) > 1:
#     print("?")
# else:
#     print(max(count, key=count.get))

# 1316
from collections import defaultdict
import sys

n = int(sys.stdin.readline())
word = [sys.stdin.readline().strip() for i in range(n)]
answer = 0

for i in word:
    count = defaultdict(int)
    count[i] += 1