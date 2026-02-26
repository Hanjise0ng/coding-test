# https://www.acmicpc.net/problem/3085
# bruteforcing silver 2

def count(lst):
    cnt = ans = 1

    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 1

    return ans

def solve(arr):
    ans = 0

    for i in range(n-1):
        for j in range(n):
            # 오른쪽 사탕과 교환
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            ans = max(ans, count(arr[i]))
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

            # 아래쪽 사탕과 교환
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            ans = max(ans, count(arr[i]), count(arr[i+1]))
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

    return ans

n = int(input())
candy = [list(input())+[0] for _ in range(n)] + [[0] * (n+1)]
candy_t = list(map(list, zip(*candy)))
print(max(solve(candy), solve(candy_t)))