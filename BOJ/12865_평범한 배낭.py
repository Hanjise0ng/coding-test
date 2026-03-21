# https://www.acmicpc.net/problem/12865
# dp gold 5

N, K = map(int, input().split())
weight = [0]
gold =[0]

for _ in range(N):
    a, b = map(int, input().split())
    weight.append(a)
    gold.append(b)
    
dp = [[0  for _ in range(K + 1)] for _ in range(N + 1)]

for n in range(1, N + 1):
    for k in range(1, K + 1):
        if k >= weight[n]:
            dp[n][k] = max(dp[n - 1][k], dp[n - 1][k - weight[n]] + gold[n])
        else:
            dp[n][k] = dp[n-1][k]

print(dp[N][K])