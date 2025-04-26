# Sort(math) Silver 3

def is_lock_valid(n, k, arr):
    groups = [[] for _ in range(k)]

    for i in range(n):
        groups[i % k].append(arr[i])
    
    for group in groups:
        group.sort()

    sorted_arr = []
    for i in range(n):
        sorted_arr.append(groups[i % k][i // k])
    
    if sorted_arr == sorted(arr):
        return "Yes"
    else:
        return "No"

n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(is_lock_valid(n, k, arr))
