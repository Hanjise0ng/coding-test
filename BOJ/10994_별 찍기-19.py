# https://www.acmicpc.net/problem/10994
# recursion silver 4

N = int(input())
stars = [[' ' for _ in range(4 * N - 3)] for _ in range(4 * N - 3)]

def draw(n, x, y):

    if n == 1:
        stars[y][x] = "*"
        return

    length = 4 * n - 3
    for i in range(length):
        stars[y][x + i] = "*"
        stars[y + i][x] = "*"
        stars[y + length - 1][x + i] = "*"
        stars[y + i][x + length - 1] = "*"

    draw(n - 1, x + 2, y + 2)

draw(N, 0, 0)

for s in stars:
    print("".join(s))
