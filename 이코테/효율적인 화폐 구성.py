n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):                                # 1. 가지고 있는 화폐 종류만큼 반복
    for j in range(array[i], m + 1):              # 2. 해당 화폐(k)로 만들 수 있는 금액부터 끝까지 반복
        if d[j - array[i]] != 10001:              # 3. (j-k)원을 만드는 방법이 존재한다면
            d[j] = min(d[j], d[j - array[i]] + 1) # 4. 더 작은 값으로 갱신

if d[m] == 10001:
    print(-1)
else:
    print(d[m])