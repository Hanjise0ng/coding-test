# https://www.acmicpc.net/problem/11780
# floyd-warshall gold 2

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
nxt = [[-1] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c
        nxt[a][b] = b

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                nxt[i][j] = nxt[i][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF or i == j:
            print(0)
            continue
        
        path = []
        curr = i
        while curr != j:
            path.append(curr)
            curr = nxt[curr][j]
        path.append(j)
        
        print(len(path), *path)