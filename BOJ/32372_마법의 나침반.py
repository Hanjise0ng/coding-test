# https://www.acmicpc.net/problem/32372
# Sliver 4

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

min_x, max_x = 1, N
min_y, max_y = 1, N

for i in range(M):
    if arr[i][2] == 1:
        max_x = min(max_x, arr[i][0] - 1)
        min_y = max_y = arr[i][1]
    elif arr[i][2] == 2:
        max_x = min(max_x, arr[i][0] - 1)
        min_y = max(min_y, arr[i][1] + 1)
    elif arr[i][2] == 3:
        min_y = max(min_y, arr[i][1] + 1)
        min_x = max_x = arr[i][0]
    elif arr[i][2] == 4:
        min_x = max(min_x, arr[i][0] + 1)
        min_y = max(min_y, arr[i][1] + 1)
    elif arr[i][2] == 5:
        min_x = max(max_x, arr[i][0] + 1)
        min_y = max_y = arr[i][1]
    elif arr[i][2] == 6:
        min_x = max(min_x, arr[i][0] + 1)
        max_y = min(max_y, arr[i][1] - 1)
    elif arr[i][2] == 7:
        max_y = min(max_y, arr[i][1] - 1)
        min_x = max_x = arr[i][0]
    elif arr[i][2] == 8:
        max_x = min(max_x, arr[i][0] - 1)
        max_y = min(max_y, arr[i][1] - 1)

print(max_x, max_y)