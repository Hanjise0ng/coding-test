# Level 2
# Greedy

def solution(people, limit):
    answer = 0
    people.sort()
    L = 0
    R = len(people) - 1
    
    while True:
        if L > R:
            break
        if people[L] + people[R] > limit:
            answer += 1
        elif people[L] + people[R] <= limit:
            answer += 1
            L += 1
        R -= 1
    return answer