n = int(input())
word = []
answer = 0
for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            new_word = word[j+1:]
            if word[j] in new_word:
                answer += 1
                break
print(n - answer)