# https://school.programmers.co.kr/tryouts/85889/challenges
# string level 1

def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        for c in can:
            if c in b:
                b = b.replace(c, "*")
        if len(b) == b.count("*"):
            answer += 1
    
    return answer