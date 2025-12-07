sen = input()
words = sen.split()
strange_words = [word for word in words if len(word) > len(set(word.lower()))]
print('-'.join(strange_words))  