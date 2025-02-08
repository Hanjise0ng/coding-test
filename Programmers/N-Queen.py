# Level 2
# DFS

def dfs(queen, row, n):
    count = 0
    
    if row == n:
        return 1
    for col in range(n):
        queen[row] = col
        
        for i in range(row):
            if queen[i] == queen[row]:
                break
            if abs(queen[i] - queen[row]) == abs(i - row):
                break
        else:
            count += dfs(queen, row + 1, n)
    return count

def solution(n):
    return dfs([0] * n, 0, n)