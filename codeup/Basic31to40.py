#31
c = int(input()) #정수값 입력받음
print(chr(c)) #유니코드 문자 출력

#32
c = int(input())
print(-c)

#33
n = input()
print(chr(ord(n) + 1))

#34
a, b = input().split()
c = int(a) - int(b)
print(c)

#35
a, b = input().split()
c = float(a) * float(b)
print(c)

#36
w, n = input().split()
print(w*int(n))

#37
#n = input()
#s = input()
#print(int(n)*s)

#38
a, b = map(int, input().split())
c = a**b
print(c)

#39
f1, f2 = map(float, input().split())
c = f1**f2
print(c)

#40
a, b = map(int, input().split())
c = a//b
print(c)