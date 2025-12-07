n = int(input())
comment = []
for _ in range(n):
    s = input()
    row = [len(s), s]
    comment.append(row)

comment.sort(reverse=True)
for i in range(0, len(comment[:]) - 1, 1):
    if comment[i][0] == comment[i + 1][0]:
        comment[i][1], comment[i + 1][1] = comment[i + 1][1], comment[i][1]


for i in range(0, len(comment)):
    print(comment[i][1])