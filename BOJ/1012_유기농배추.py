# graph silver 2
# dfs 방식
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    for a in arr:
        print(a)
    print()
    arr[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 1:
                dfs(nx,ny)  
answer = []
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    cnt = 0
    
    for _ in range(k):
        y, x = map(int, input().split())
        arr[x][y] = 1
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                dfs(i,j)
                cnt += 1
    answer.append(cnt)

for a in answer:
    print(a)

#bfs 방식
answer = []
t = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = [(x,y)]
    arr[x][y] = 0

    while queue:
        x,y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    queue.append((nx,ny))
                    arr[nx][ny] = 0

for _ in range(t):
    m,n,k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        y,x = map(int, input().split())
        arr[x][y] = 1
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                bfs(i,j)
                cnt += 1

    answer.append(cnt)

for a in answer:
    print(a)