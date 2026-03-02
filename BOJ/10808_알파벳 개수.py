# https://www.acmicpc.net/problem/10808
# string bronze 4

s = input()
arr = [0] * 26

for x in s:
    i = ord(x) - ord('a')
    arr[i] += 1

print(*arr)