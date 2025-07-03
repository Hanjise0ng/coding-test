# https://www.acmicpc.net/problem/1715
# greedy gold 4

import heapq

N = int(input())
card = [int(input()) for _ in range(N)]

heapq.heapify(card)

res = 0

while len(card) != 1:
    A = heapq.heappop(card)
    B = heapq.heappop(card)
    heapq.heappush(card, A + B)

    res += A + B

print(res)