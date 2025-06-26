# https://school.programmers.co.kr/learn/courses/30/lessons/60057
# brute force level 2

def solution(s):
    answer = len(s)
    
    for i in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0 : i]    # 앞에서부터 i 만큼의 문자열 추출
        cnt = 1
        
        # 단위 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(i, len(s), i):
            
            # 이전 상태와 도일하다면 압축 횟수(cnt) 증가
            if prev == s[j : j + i]:
                cnt += 1
                
            else:
                if cnt >= 2:
                    compressed += str(cnt) + prev
                else:
                    compressed += prev
                
                # 상태 초기화
                prev = s[j : j + i]
                cnt = 1
                
        # 남아 있는 문자열에 대해서 처리
        compressed += str(cnt) + prev if cnt >= 2 else prev
        
        answer = min(answer, len(compressed))
        
    return answer
