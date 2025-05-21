# https://www.acmicpc.net/problem/17130
# DP Gold 4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
dp = [[-1] * M for _ in range(N)]

# 토끼 시작 위치 찾기
Rx, Ry = -1, -1 
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R': # 토끼
            Rx, Ry = i, j
            break

# 재귀 탐색
def func(x, y):
    temp = -10000000
    d = ((1, 1), (0, 1), (-1, 1)) # 이동 방향

    for dx, dy in d:
        if -1 < x + dx < N and -1 < y + dy < M: # 범위
            if arr[x + dx][y + dy] == '#': # 벽, continue
                continue

            if arr[x + dx][y + dy] == 'C': # 당근, 현재 값과 이동하기 전의 값 + 1 을 비교
                if dp[x + dx][y + dy] != -1:
                    temp = max(temp, dp[x + dx][y + dy] + 1)
                else:
                    temp = max(temp, func(x + dx, y + dy) + 1)
                
            elif arr[x + dx][y + dy] == 'O': # 쪽문, 현재 값과 이동하기 전의 값을 비교
                if dp[x + dx][y + dy] != -1:
                    temp = max(temp, 0, dp[x + dx][y + dy])
                else:
                    temp = max(temp, 0, func(x + dx, y + dy))

            else: # . : 빈 공간, 현재 값과 이동하기 전의 값을 비교
                if dp[x + dx][y + dy] != -1:
                    temp = max(temp, dp[x + dx][y + dy])
                else:
                    temp = max(temp, func(x + dx, y + dy))

    dp[x][y] = temp
    return dp[x][y]

func(Rx, Ry)

if dp[Rx][Ry] < 0:
    print(-1)
else:
    print(dp[Rx][Ry])
