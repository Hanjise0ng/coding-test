# https://www.acmicpc.net/problem/2839
# dp silver 4

n = int(input())

INF = int(10e9)
dp = [INF] * (5001)

dp[3] = 1
dp[5] = 1

for i in range(6, n + 1):
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1

if dp[n] < INF:
    print(dp[n])
else:
    print(-1)