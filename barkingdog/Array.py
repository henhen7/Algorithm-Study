##Q02.
# 문제: 주어진 길이 N의 int 배열 arr에서 합이 100인 서로 다른 위치의 두 원소가 존재하면 1을,
#      존재하지 않으면 0을 반환하는 함수 func2(int arr[], int N)을 작성하라.
#      arr의 각 수는 0 이상 100 이하이고, N은 1000 이하이다.

def func2(arr, N):
    for i in range(N):
        for j in range(i+1, N):
            if arr[i] + arr[j] == 100:
                return 1
    return 0

print(func2([52, 2, 48], 3))
