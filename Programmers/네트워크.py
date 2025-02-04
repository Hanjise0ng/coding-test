# Level 3
# DFS/BFS

def dfs(n, computers, visited, i):
    if visited[i] == 1:
        return
    else:
        visited[i] = 1

        for j in range(n):
            if i != j and computers[i][j] == 1:
                dfs(n, computers, visited, j)

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for i in range(n):
        if visited[i] == 0:
            dfs(n, computers, visited, i)
            answer += 1
    
    return answer