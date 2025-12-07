n = int(input())
words = []
for _ in range(n):
    s = input()
    row = [len(set(s)), s]
    words.append(row)

words.sort(reverse=True)
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if words[i][0] == words[j][0] and words[i][1] > words[j][1]:
            words[i], words[j] = words[j], words[i]

for i in range(len(words)):
    print(words[i][1])
