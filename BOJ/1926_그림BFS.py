# https://www.acmicpc.net/problem/1926
# BFS Sliver 1

from collections import deque

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(arr, a, b):
    q = deque()
    q.append((a,b))

    arr[a][b] = 0
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] ==1:
                arr[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

res = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            res.append(bfs(arr, i, j))

if len(res) == 0:
    print(0)
    print(0)
else:
    print(len(res))
    print(max(res))