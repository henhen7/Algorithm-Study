#51
a, b = map(int, input().split())
print(a != b)

#52
a = int(input())
print(bool(a))

#53
a = bool(int(input()))
print(not a)

#54
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

#55
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

#56
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

#57
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print(c == d)

#58
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c == 0) and (d == 0))

#59
a = int(input())
print(~a)

#60
# 비트단위(bitwise)연산자
# ~(bitwise not), &(bitwise and)
# |(bitwise or), ^(bitwise xor)
# <<(bitwise left shift), >>(bitwise right shift)
a, b = map(int, input().split())
print(a & b)