n = int(input())
m = int(input())
li = list(map(int, input().split()))

result = []

for i in li:
    if i not in [x[0] for x in result]:
        if len(result) < n:
            result.append([i, 1])
        else:
            min_li = min(result, key=lambda x: x[1])
            result.remove(min_li)
            result.append([i, 1])
    else:
        for j in range(len(result)):
            if result[j][0] == i:
                result[j][1] += 1
                break

result.sort()
for i in result:
    print(i[0], end = ' ')