#Q1. 시간복잡도: O(N)
def func1(k):
    ans = 0
    for i in range(k):
        if (i % 3 == 0 or i % 5 == 0):
            ans = ans + i
    return ans

print(func1(16))

#Q2. 시간복잡도: O(N^2)
def func2(arr, N):
    for i in range(N):
        for j in range(i+1, N):
            if arr[i] + arr[j] == 100:
                return 1
    return 0

print(func2([1,52,48], 3))

#Q3. 시간복잡도: O(sqrt(N))
def func3(N):
    for i in range(N):
        if (i*i == N):
            return 1
    return 0

print(func3(756580036))

#Q4. 시간복잡도: O(lgN)
def func4(N):
    val = 1
    while 2 * val <= N: #끝나는 조건을 알 때 반복문
        val *= 2
    return val

print(func4(97615282))