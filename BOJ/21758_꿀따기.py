# Greedy Gold 5

import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))

h = sum(m[:])
t = m[0]
ans = 0
a, b, c = 0, 0, 0

# b - b - h
for i in range(1, n):
    t += m[i]
    a = max(a, 2 * h - m[0] - t - m[i])

# h - b - b
m.reverse()
t = m[0]
for i in range(1, n):
    t += m[i]
    b = max(b, 2 * h - m[0] - t - m[i])

# b - h - b
for i in range(1, n):
    c = max(c, h - m[0] - m[-1] + m[i]) # 모든 곳에 꿀을 한번씩 먹고 꿀통 지점의 꿀을 한번 더 먹는다.

ans = max(a, b, c)
print(ans)