#61
a, b = map(int, input().split())
print(a | b)

#62
a, b = map(int, input().split())
print(a ^ b)

#63
a, b = map(int, input().split())
print(a if (a >= b) else b) #3항연산

#64
a, b, c = map(int, input().split())
ans = (a if a < b else b) if ((a if a < b else b) < c) else c
print(ans)

#65
a, b, c = map(int, input().split())
if a%2 == 0:
    print(a)
if b%2 == 0:
    print(b)
if c%2 == 0:
    print(c)

#66
a, b, c = map(int, input().split())
if a%2 == 0:
    print("even")
else:
    print("odd")

if b%2 == 0:
    print("even")
else:
    print("odd")

if c%2 == 0:
    print("even")
else:
    print("odd")

#67
n = int(input())
if n < 0:
    if n % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if n % 2 == 0:
        print('C')
    else:
        print('D')

#68
n = int(input())
if n >= 90:
    print('A')
else:
    if n >= 70:
        print('B')
    else:
        if n >= 40:
            print('C')
        else:
            print('D')

#69
n = input()
if n == 'A':
    print('best!!!')
else:
    if n == 'B':
        print('good!!')
    else:
        if n == 'C':
            print('run!')
        else:
            if n == 'D':
                print('slowly~')
            else:
                print('what?')

#70
n = int(input())
if n in [12, 1, 2]:
    print('winter')
else:
    if n in [3, 4, 5]:
        print('spring')
    else:
        if n in [6, 7, 8]:
            print('summer')
        else:
            print('fall')