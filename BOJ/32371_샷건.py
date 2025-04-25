# Brute force Bronze 1

arr = [list(map(str,input().rstrip())) for _ in range(4)]
ll = list(map(str,input().rstrip()))

l = []
for k in range(len(ll)):
    for i in range(4):
        for j in range(10):
            if arr[i][j] == ll[k]:
                l.append((i, j))
        
l.sort()
x, y = l[4]
print(arr[x][y])