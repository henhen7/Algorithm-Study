#71
n = 1
while n != 0:
    n = int(input())
    if n == 0:
        break
    print(n)

#72
n = int(input())
while n != 0:
    print(n)
    n -= 1

#73
n = int(input())
while n != 0:
    print(n-1)
    n -= 1

#74
a = ord(input())
t = ord('a')
while t <= a:
    print(chr(t), end = ' ')
    t += 1

#75
n = int(input())
a = 0
while n >= a:
    print(a)
    a += 1

#76
n = int(input())
for i in range(n+1):
    print(i)

#77
n = int(input())
sum = 0
for i in range(n+1):
    if i%2 == 0:
        sum += i
print(sum)

#78
a = 1
while a != ord('q'):
    a = ord(input())
    print(chr(a))

#79
n = int(input())
sum = 0
for i in range(n+1):
    if sum >= n:
        break
    sum += i

print(i - 1)

#80
n, m = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)