# https://www.acmicpc.net/problem/2133
# dp gold 4

n =  int(input())

dp = [0] * 31
dp[0], dp[2] = 1, 3

for i in range(4, n + 1, 2):
    dp[i] = dp[i - 2] * 3

    for j in range(i - 4, -1, -2):
        dp[i] += dp[j] * 2

print(dp[n])