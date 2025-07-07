# https://www.acmicpc.net/problem/24060
# sort sliver 3

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = (len(arr)+1) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sort = merge_sort(left)
    right_sort = merge_sort(right)
    return merge(left_sort, right_sort)

def merge(left_sort, right_sort):
    i, j = 0, 0
    list_sort = []

    while i < len(left_sort) and j < len(right_sort):
        if left_sort[i] < right_sort[j]:
            list_sort.append(left_sort[i])
            answer.append(left_sort[i])
            i += 1
        else:
            list_sort.append(right_sort[j])
            answer.append(right_sort[j])
            j += 1

    while i < len(left_sort):
        list_sort.append(left_sort[i])
        answer.append(left_sort[i])
        i += 1
    while j < len(right_sort):
        list_sort.append(right_sort[j])
        answer.append(right_sort[j])
        j += 1
    return list_sort

n, k = map(int, input().split())
A = list(map(int, input().split()))
answer = [] # 새로운 리스트 선언
merge_sort(A) # 배열을 병합정렬 함수 안에 대입

if len(answer) >= k: # 길이가 k보다 크거나 같으면
    print(answer[k-1]) # 인덱스는 0부터 시작하니 k-1번째를 출력
else:
    print(-1) # 길이가 k보다 작으면 -1 출력