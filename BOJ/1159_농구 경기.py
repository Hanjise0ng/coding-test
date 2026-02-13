# https://www.acmicpc.net/problem/1159
# string bronze 2

n = int(input())
players = []
ans = []

for _ in range(n):
    x = input()
    players.append(x[0])

first = set(players)

for f in first:
    if players.count(f) >= 5:
        ans.append(f)

if len(ans) > 0:
    print(''.join(sorted(ans)))
else:
    print("PREDAJA")