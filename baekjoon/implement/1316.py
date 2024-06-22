# # 1316
# import sys
#
# n = int(sys.stdin.readline())
# word = [sys.stdin.readline().strip() for i in range(n)]
# answer = 0
#
# for i in len(word):
#     print(i)
#
n = int(input())
word = []
answer = 0
for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            new_word = word[j+1:]
            if word[j] in new_word:
                answer -= 1
                break
    answer += 1
print(answer)