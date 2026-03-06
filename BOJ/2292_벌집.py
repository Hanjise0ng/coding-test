# https://www.acmicpc.net/problem/2292
# math bronze 2

n = int(input())

cnt = 1
ans = 1
while cnt < n:
    cnt += ans * 6
    ans += 1

print(ans)