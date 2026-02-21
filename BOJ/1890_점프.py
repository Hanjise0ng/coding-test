# https://www.acmicpc.net/problem/1890
# dp silver 1

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):

        if matrix[i][j] == 0:
            continue

        jump = matrix[i][j]

        if i + jump < n: # 아래쪽으로 점프
            dp[i + jump][j] += dp[i][j]

        if j + jump < n: # 오른쪽으로 점프
            dp[i][j + jump] += dp[i][j]

print(dp[n - 1][n - 1])