# https://www.acmicpc.net/problem/16227
# floyd-warshall gold 2

from heapq import heappop, heappush 

mii = lambda : map(int, input().split())
n, k = mii()
MAX_TIME = 100
DELAY_TIME = 5
INF = float("INF")

arr = [[] for _ in range(n + 2)]

for _ in range(k):
    u, v, t = mii()
    if MAX_TIME < t:
        continue

    arr[u].append((v, t))
    arr[v].append((u, t))

def dijkstra(S, E):
    time = [INF] * (n + 2)
    q = [(0, 0, S)]
    time[S] = 0

    while q:
        cur_time, used_time, cur_node = heappop(q)

        if time[cur_node] < cur_time:
            continue

        for nxt_node, nxt_time in arr[cur_node]:
            check_time = used_time + nxt_time
            total_time = cur_time + nxt_time

            if MAX_TIME < check_time:
                check_time = nxt_time
                total_time += DELAY_TIME

            if total_time < time[nxt_node]:
                time[nxt_node] = total_time
                heappush(q, (total_time, check_time, nxt_node))

    return time[E]

print(dijkstra(0, n + 1))