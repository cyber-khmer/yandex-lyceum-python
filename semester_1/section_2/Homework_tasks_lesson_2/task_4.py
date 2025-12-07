winners = []
new_winners = []
while (name := input()) != '':
    winners.append(name)

maxi = []
for el in winners:
    maxi.append(winners.count(el))

for i in range(len(maxi)):
    if maxi[i] == max(maxi) and winners[i] not in new_winners:
        new_winners.append(winners[i])

print(*sorted(new_winners), sep=' ')