# Level 3
# DP

def solution(N, number):
    if N == number:
        return 1
    
    dp = [0, {N}]
    
    for i in range(2, 9):
        case = {int(str(N) * i)}
        
        for i_half in range(1, (i // 2) + 1):
            for x in dp[i_half]:
                for y in dp[i-i_half]:
                    case.add(x+y)
                    case.add(x-y)
                    case.add(y-x)
                    case.add(x*y)
                    
                    if x != 0:
                        case.add(y//x)
                    if y != 0:
                        case.add(x//y)
                        
        if number in case:
            return i
        
        dp.append(case)
            
    return -1