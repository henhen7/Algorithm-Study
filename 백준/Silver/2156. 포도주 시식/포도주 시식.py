n = int(input())

li = []

for i in range(n):
    li.append(int(input()))

d = [0]*n

d[0] = li[0]
if n > 1:
    d[1] = li[0]+li[1]

if n > 2:
    d[2] = max(li[2]+li[1], li[2]+li[0], d[1])

for i in range(3, n):
    d[i] = max(d[i-1], d[i-3]+li[i-1]+li[i], d[i-2]+li[i])

print(d[n-1])