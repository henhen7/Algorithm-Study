from collections import Counter

n, k = map(int, input().split())
li = list(map(int, input().split()))

left = 0
right = 0
ans = 1
arr = []

while right < n - 1:
    right += 1
    arr.append(li[right])
    # print(max(Counter(arr).values()))
    while max(Counter(arr).values()) > k:
        arr.pop(left)
        left += 1
        ans = max(ans, right - left + 1)
print(ans)