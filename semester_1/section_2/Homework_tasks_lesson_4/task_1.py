s = input().split('-')
word = input()
if word in s:
    print(s.index(word))
else:
    print(-1)