# https://school.programmers.co.kr/learn/courses/30/lessons/340212?language=python3
# https://59travel.tistory.com/83#google_vignette
# binary search level 2

def puzzle(diffs, times, limit, level):
    
    clear_time = 0

    for idx in range(len(diffs)):
        if diffs[idx] <= level: clear_time += times[idx]
        if diffs[idx] > level: clear_time += (diffs[idx] - level) * (times[idx - 1] + times[idx]) + times[idx]
        if clear_time > limit: return False
    
    return True
 
def solution(diffs, times, limit):
    
    start, mid, end = 1, 0, max(diffs)
 
    while start <= end:
        mid = (start + end) // 2
        
        if puzzle(diffs, times, limit, mid): end = mid - 1
        else: start = mid + 1
    
    ## start : 1, mid : 1, end : 2 인 경우
    if puzzle(diffs, times, limit, mid): return mid
    if puzzle(diffs, times, limit, mid+1): return mid + 1

    return mid - 1

# print(solution([1, 5, 3], [2, 4, 7], 30))
# print(solution([1, 4, 4, 2], [6, 3, 8, 2], 59))
# print(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723))
# print(solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012))