s = input().split()
words_unique = set()
for w in s:
    words_unique.add(''.join(set(w)))

print(words_unique)