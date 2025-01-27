# https://www.acmicpc.net/problem/24525
# Gold 3

s = input()
n = len(s)

skk = [0 for _ in range(1000000)]
idx = [-1 for _ in range(1000000)]
idx[1] = 0

ans = -1
cnt = 0

for i in range(1, n + 1):
    if s[i - 1] == 'S':
        skk[i] = skk[i - 1] + 1
        cnt += 2

    elif s[i - 1] == 'K':
        skk[i] = skk[i - 1] + 1
        cnt -=1

    else:
        skk[i] = skk[i - 1]

    if idx[cnt + 1] == -1:
        idx[cnt + 1] = i

    elif skk[i] - skk[idx[cnt + 1]] > 0:
        ans = max(ans, i - idx[cnt + 1])


if ans > 0:
    print(ans)
else:
    print(-1)
