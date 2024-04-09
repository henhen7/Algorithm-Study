'''
#81
n = int(input(), base = 16)
for i in range(1, 16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

#82
n = int(input())
for i in range(1, n+1):
    if i%10 in (3, 6, 9):
        print("X", end=' ')
    else:
        print(i, end = ' ')

#83
r, g, b = map(int, input().split())
for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(i, j, k)
print(r*g*b)

#84
h, b, c, s = map(int, input().split())
ans = h*b*c*s/8/1024/1024
print(round(ans, 1), 'MB')

#85
w, h, b = map(int, input().split())
ans = w*h*b/8/1024/1024
print(round(ans, 2), 'MB')

#86
n = int(input())
sum = 0
for i in range(n+1):
    if sum >= n:
        break
    sum += i

print(sum)

#87
n = int(input())
for i in range(1, n+1):
    if i%3 == 0:
        continue
    print(i, end = ' ')

#88
a, d, n = map(int, input().split())
ans = a
for i in range(n):
    if i == 0:
        continue
    ans += d
print(ans)

#89
a, r, n = map(int, input().split())
ans = a
for i in range(n):
    if i == 0:
        continue
    ans = a*r**(n-1)
print(ans)
'''
#90
a, m, d, n = map(int, input().split())
ans = a
for i in range(n-1):
    ans = ans * (m) + d
print(ans)