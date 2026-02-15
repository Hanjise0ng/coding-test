# https://www.acmicpc.net/problem/2156
# dp silver 1

n = int(input())

wine = []

for i in range(n):
    wine.append(int(input()))

dp = [0] * n

dp[0] = wine[0]
if n > 1:
    dp[1] = wine[0] + wine[1]

if n > 2:
    dp[2] = max(wine[2] + wine[1], wine[2] + wine[0], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i])

print(dp[n - 1])

