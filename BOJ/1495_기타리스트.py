# https://www.acmicpc.net/problem/1495
# dp silver 1

n, s, m = map(int, input().split())
v = list(map(int, input().split()))

# d[i][j] :i번째 곡을 j볼륨으로 만들 수 있는지 여부 (1:가능/0:불가능)
dp=[[0] * (m + 1) for _ in range(n + 1)]
# 첫번째 곡은 s 볼륨으로 시작 가능
dp[0][s] = 1

for i in range(1, n + 1): # 곡 개수
    for j in range(m + 1): # 최대 볼륨까지 확인
        if dp[i - 1][j] != 0: # 이전 단계 볼륨 조절 가능했다면
            if 0 <= j + v[i - 1] <= m: # 볼륨 조절 후 범위 안에 있으면 1 추가
                dp[i][j + v[i - 1]] = 1 # i번째 가능했던 볼륨들 체크
            if 0 <= j - v[i - 1] <= m:
                dp[i][j - v[i - 1]] = 1

ans = -1
# n 번째까지 볼륨 조절이 가능했다면 내림차순으로 최대값 구하기
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        ans = i
        break

print(ans)

