# Level 3
# Heap

import heapq

def solution(jobs):
    now, tmp = 0, 0
    start, waiting = -1, 0
    heap = []

    jobs.sort()

    while tmp < len(jobs):
        for job in jobs[tmp: ]:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        if heap:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            waiting += (now - current[1])
            tmp += 1
        else:
            now += 1

    ans = int(waiting / len(jobs))
    return ans