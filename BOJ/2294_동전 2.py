# https://www.acmicpc.net/problem/2294
# dp gold 5

n, k = map(int, input().split())
INF = float("INF")

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [[INF] * (k + 1) for _ in range(n)]

for i in range(n):
    dp[n][0] = 0
    for k in range(1, k + 1):
        case1 = INF
        prev_k = k - coins[i]
        if 0 <= prev_k:
            case1 = dp[n][prev_k] + 1
        case2 = dp[i - 1][k]
        dp[i][k] = min(case1, case2)

if dp[n - 1][k] == INF:
    print(-1)
else:
    print(dp[n - 1][k])