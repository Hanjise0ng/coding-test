# # https://www.acmicpc.net/problem/2502
# # dp silver 1

def fibo(d):
    dp = [[0, 0] for _ in range(d + 1)]
    dp[1] = [1, 0]
    dp[2] = [0, 1]
    for i in range(3, d + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

    return dp[d]

d, k = map(int, input().split())

dp = fibo(d)

for a in range(1, k):
    if (k - dp[0] * a) % dp[1] == 0:
        b = (k - dp[0] * a) // dp[1]
        print(a)
        print(b)
        break