import sys
input = sys.stdin.readline

def binary_search(arr, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
x = list(map(int, input().split()))

result = []
for i in x:
    find = binary_search(arr, i, 0, n - 1)
    if find != None:
        result.append("yes")
    else:
        result.append("no")

print(*result) # print(" ".join(result))