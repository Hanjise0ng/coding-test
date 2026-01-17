n = int(input())

arr = []
for i in range(n):
    name, score = input().split()
    arr.append((name, int(score)))

arr = sorted(arr, key = lambda x: x[1])

for s in arr:
    print(s[0], end=' ')