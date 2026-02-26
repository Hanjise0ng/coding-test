# https://www.acmicpc.net/problem/3085
# bruteforcing silver 2

def count(rows, cols):
    ans = 1
    
    for i in rows:
        cnt = 1
        for j in range(1, n):
            if candy[i][j] == candy[i][j-1]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
                
    for j in cols:
        cnt = 1
        for i in range(1, n):
            if candy[i][j] == candy[i-1][j]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
                
    return ans

n = int(input())
candy = [list(input().strip()) for _ in range(n)]

ans = count(range(n), range(n))

for i in range(n):
    for j in range(n):
        # 오른쪽 사탕과 교환
        if j + 1 < n and candy[i][j] != candy[i][j+1]:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            ans = max(ans, count([i], [j, j+1]))
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            
        # 아래쪽 사탕과 교환
        if i + 1 < n and candy[i][j] != candy[i+1][j]:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            ans = max(ans, count([i, i+1], [j]))
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(ans)