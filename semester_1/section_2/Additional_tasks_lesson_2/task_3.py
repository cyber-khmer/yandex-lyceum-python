n = int(input())
sentences = []
for i in range(n):
    sentences.append(input())

item = int(input())
it = 0
for i in range(item):
    for j in range(len(sentences)):
        if it % 2 == 0:
            print(sentences[j].lower())
        else:
            print(sentences[j].upper())
        it += 1