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