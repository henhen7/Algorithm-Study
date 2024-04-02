#41
a, b = map(int, input().split())
print(a%b)

#42
a = float(input())
print(format(a, ".2f"))

#43
f1, f2 = map(float, input().split())
print(format(f1/f2, ".3f"))

#44
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(format(float(a / b), ".2f"))

#45
a, b, c = map(int, input().split())
sum = a + b + c
mean = float(sum/3)
print(sum, format(mean, ".2f"))

#46
a = int(input())
print(a<<1)

#47
a, b = map(int, input().split())
print(a<<b)

#48
a, b = map(int, input().split())
print(a<b)

#49
a, b = map(int, input().split())
print(a==b)

#50
a, b = map(int, input().split())
print(a<=b)