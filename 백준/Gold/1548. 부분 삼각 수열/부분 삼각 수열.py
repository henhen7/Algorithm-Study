n = int(input())
li = sorted(list(map(int,input().split())))

if n > 2:
    ans = 2
    for i in range(n - 2):
        end = i + 2
        while True:
            if li[i] + li[i + 1] > li[end]:
                ans = max(ans, end - i + 1)
                end += 1
                if end == n:
                    break
            else:
                break
    print(ans)
# 예제 1, 5의 경우, 삼각 수열을 이루는 수열의 원소가 3보다 작으면 그냥 원소의 개수 반환
else:
    print(n)