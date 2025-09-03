# https://school.programmers.co.kr/learn/courses/30/lessons/250136
# dfs level 2

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(r, c, matrix, visited, cols):
    n, m = len(matrix), len(matrix[0])
    queue = deque([(r, c)])
    visited[r][c] = True
    result = 0

    cols_set = set()

    while queue:
        y, x = queue.popleft()
        cols_set.add(x)
        result += 1

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and matrix[ny][nx] == 1:
                queue.append((ny, nx))
                visited[ny][nx] = True

    for col in cols_set:
        cols[col] += result

def solution(land):
    n, m =  len(land), len(land[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    cols = [0 for _ in range(m)]

    for r in range(n):
        for c in range(m):
            if land[r][c] == 1 and not visited[r][c]:
                bfs(r, c, land, visited, cols)

    return max(cols)