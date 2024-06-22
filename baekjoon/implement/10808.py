### 10808
# 문제: 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 리스트에 모두 입력하는 방법
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z"]

ex = []
n = str(input())

for i in n:
    ex.append(i)

for i in alphabet:
    print(ex.count(i), end = " ")

# 아스키 코드를 사용하는 방법
s = input()
arr = [0]*26
for i in s:
    arr[ord(i)-97] += 1 #ord('a'): 97이므로 97을 빼서 0으로 만들어 줌
print(*arr)