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