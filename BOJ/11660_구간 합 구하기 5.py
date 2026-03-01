# https://www.acmicpc.net/problem/11660
# prefix sum silver 1

n, m = map(int, input().split())

arr = [0]
for _ in range(n):
    line = [0] + list(map(int, input().split()))
    arr.append(line)

sum_arr = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum_arr[i][j] = arr[i][j]
        sum_arr[i][j] += sum_arr[i][j - 1] + sum_arr[i - 1][j]
        sum_arr[i][j] -= sum_arr[i - 1][j - 1]

for _ in range(m):
    i1, j1, i2, j2 = map(int, input().split())
    ans = sum_arr[i2][j2]
    ans -= sum_arr[i2][j1 - 1]
    ans -= sum_arr[i1 - 1][j2]
    ans += sum_arr[i1 - 1][j1 - 1]

    print(ans)