# https://www.acmicpc.net/problem/5430
# implementation gold 5

from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    x = deque(input()[1:-1].split(',')) # 입력받은 배열 양방향 큐에 담기
    
    if n == 0:  # deque[''] 의 길이를 0이 아닌 1로 취급
        x = []

    r = 0 # 뒤집힌 상태 체크

    for i in p:
        if i == 'R':
            r += 1
        elif i == 'D':
            if len(x) == 0:
                print('error')
                break
            else:
                if r % 2 == 1:
                    x.pop()
                else:
                    x.popleft()
                        
    else:
        if r % 2 == 1: # 최종 뒤집힌 상태 반영
            x.reverse()
        print('[' + ','.join(x) + ']')