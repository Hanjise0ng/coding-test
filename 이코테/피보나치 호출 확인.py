d = [0] * 100

def fibo(x):
    print("f(" + str(x) + ")", end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

# 탑다운 방식으로 피보나치 함수 호출
fibo(6)