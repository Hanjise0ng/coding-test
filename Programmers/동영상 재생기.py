# https://school.programmers.co.kr/learn/courses/30/lessons/340213
# string level 1

def solution(video_len, pos, op_start, op_end, commands):
    mm, ss = map(int, pos.split(":"))
    end_mm, end_ss = map(int, video_len.split(":"))
    op_start_mm, op_start_ss = map(int, op_start.split(":"))
    op_end_mm, op_end_ss = map(int, op_end.split(":"))
    
    def skip_opening(mm, ss):
        if (op_start_mm < mm == op_end_mm and ss < op_end_ss) or \
           (op_start_mm < mm < op_end_mm) or \
           (op_start_mm == mm == op_end_mm and op_start_ss <= ss < op_end_ss) or \
           (op_start_mm == mm < op_end_mm and op_start_ss <= ss):
            return op_end_mm, op_end_ss
        return mm, ss
    
    mm, ss = skip_opening(mm, ss)
    
    for c in commands:
        if c == "prev":
            if (ss - 10 < 0) and (mm >= 1): 
                mm -= 1
                ss = 60 + (ss - 10)
            else:
                ss = max(0, ss - 10)
                
        if c == "next":
            if (ss + 10 >= 60) and (mm < end_mm): mm += 1
            if mm == end_mm:
                ss = min((ss + 10) % 60, end_ss)
            else:
                ss = (ss + 10) % 60
                
        mm, ss = skip_opening(mm, ss)
    
    return str(mm).zfill(2) + ":" + str(ss).zfill(2)