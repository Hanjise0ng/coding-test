# https://www.acmicpc.net/problem/1513
# dp gold 2

import sys
input = sys.stdin.readline

# N: 세로, M: 가로, C: 오락실 개수
N, M, C = map(int, input().split())

# 지도 정보 초기화 (1번 인덱스부터 사용하기 위해 N+1, M+1 크기 생성)
# 0이면 일반 길, 1~C는 해당 번호의 오락실
board = [[0] * (M + 1) for _ in range(N + 1)]

# 오락실 위치 입력 받기
for i in range(1, C + 1):
    r, c = map(int, input().split())
    board[r][c] = i  # 지도에 오락실 번호 마킹

# 4차원 DP 배열 생성
# dp[x][y][count][last]
# x, y: 현재 좌표
# count: 현재까지 방문한 오락실 개수 (0 ~ C)
# last: 마지막으로 방문한 오락실 번호 (0 ~ C, 0은 방문 안 함을 의미)
dp = [[[[0] * (C + 1) for _ in range(C + 1)] for _ in range(M + 1)] for _ in range(N + 1)]

MOD = 1000007

if board[1][1] == 0:
    # 시작점이 일반 길인 경우: 방문 개수 0, 마지막 번호 0
    dp[1][1][0][0] = 1
else:
    # 시작점이 오락실인 경우: 방문 개수 1, 마지막 번호는 해당 오락실 번호
    dp[1][1][1][board[1][1]] = 1

for i in range(1, N + 1):
    for j in range(1, M + 1):
        # 시작점은 이미 처리했으므로 건너뜀
        if i == 1 and j == 1:
            continue
        
        # 현재 위치가 오락실인지 확인
        curr_arcade = board[i][j]
        
        # 일반 길(0)인 경우
        if curr_arcade == 0:
            for count in range(C + 1): # 방문 개수 0개부터 C개까지
                for last in range(C + 1): # 마지막 방문 번호 0~C번
                    # 위쪽(i-1, j)과 왼쪽(i, j-1)에서 오는 경우의 수를 합산
                    # 일반 길이므로 count last는 변하지 않음
                    dp[i][j][count][last] = (dp[i-1][j][count][last] + dp[i][j-1][count][last]) % MOD
        
        # 오락실인 경우
        else:
            # 오락실을 방문하게 되므로 방문 개수(count)는 최소 1개부터 시작
            for count in range(1, C + 1):
                # 규칙: 이전 오락실 번호(prev_last)는 현재 오락실 번호(curr_arcade)보다 작아야 함
                for prev_last in range(curr_arcade):
                    # 위쪽과 왼쪽에서, '방문 개수가 하나 적고', '번호가 작은' 경로들을 합산
                    dp[i][j][count][curr_arcade] += (dp[i-1][j][count-1][prev_last] + dp[i][j-1][count-1][prev_last])
                    dp[i][j][count][curr_arcade] %= MOD

# 도착점 (N, M)에서 방문 횟수 k(0~C)인 모든 경우의 수 출력
result = []
for k in range(C + 1):
    total_paths = sum(dp[N][M][k]) % MOD
    result.append(str(total_paths))

print(" ".join(result))