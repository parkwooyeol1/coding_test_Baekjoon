N = int(input().strip())
count = N
for i in range(N):
    check_words = [] 
    word = input().strip()
    for j in range(len(word)):
        if len(check_words) == 0:
            check_words.append(word[j])
        elif word[j] not in check_words[0:j-1]:
            check_words.append(word[j])
        elif word[j] == word[j-1]:
            check_words.append(word[j])
        else: 
            count -= 1
            break
print(count)