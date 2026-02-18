# https://www.acmicpc.net/problem/2747
# dp bronze 2

n = int(input())

a, b = 0, 1

for i in range(n):
    a, b = b, a + b

print(a)