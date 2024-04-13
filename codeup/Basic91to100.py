#91
a, b, c = map(int, input().split())
d = 1
while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1
print(d)

#92
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

m = []
for i in range(1, 24):
    m.append(0)

for i in range(n):
    m[a[i]-1] += 1

print(*m)

#93
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

print(*a[::-1])

#94
n = int(input())
a = input().split()
min = 10000

for i in range(n):
    a[i] = int(a[i])
    if a[i] < min:
        min = a[i]

print(min)

#95
d = [[0 for j in range(20)] for i in range(20)]
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    d[x][y] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end = ' ')
    print()

#96
d = [[0 for j in range(20)] for i in range(20)]
for i in range(1, 20):
    d.append(list(map(int, input().split())))

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(1, 20):
        if d[j][y] == 0:
            d[j][y] = 1
        else:
            d[j][y] = 0
        if d[x][j] == 0:
            d[x][j] = 1
        else:
            d[x][j] = 0

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end = ' ')
    print()

#97