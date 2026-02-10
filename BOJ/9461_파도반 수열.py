# https://www.acmicpc.net/problem/9461
# dp silver 3

dp = [0, 1, 1, 1, 2, 2, 3, 4, 5] + [0 for _ in range(100)]

for i in range(9, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

t = int(input())
for _ in range(t):
    print(dp[int(input())])