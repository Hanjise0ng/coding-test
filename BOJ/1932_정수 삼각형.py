# https://www.acmicpc.net/problem/1932
# dp silver 1

n = int(input())
dp = [list(map(int, input().rstrip().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0: # 처음
            dp[i][j] += dp[i - 1][j]
        elif j == i: # 끝
            dp[i][j] += dp[i - 1][j - 1]
        else: # 중간
            dp[i][j] += max(dp[i - 1][j], dp[i - 1][j - 1])

print(max(dp[n - 1]))