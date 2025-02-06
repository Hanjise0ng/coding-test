# Level 2
# Greedy

def solution(number, k):
    answer = ''
    stk = []
    
    for i in number:
        while stk and stk[-1] < i and k > 0:
            k-=1
            stk.pop()
        stk.append(i)
        
    answer = "".join(stk[:len(stk) - k])
    return answer