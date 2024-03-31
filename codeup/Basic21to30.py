#21
#s = input()
#for i in range(5):
#print(s[i])

#22
ymd = input()
print(ymd[0:2], ymd[2:4], ymd[4:6])

#23
t, m, s = input().split(':')
print(m)

#24
w1, w2 = input().split()
s = w1+w2
print(s)

#25
a, b = input().split()
c = int(a) + int(b)
print(c)

#26
a = input()
b = input()
print(float(a) + float(b))

#27
a = input()
n = int(a)
print('%x'%n)

#28
a = input()
n = int(a)
print('%X'%n)

#29
a = input()
n = int(a, 16)
print('%o'%n)

#30
n = ord(input())
print(n)