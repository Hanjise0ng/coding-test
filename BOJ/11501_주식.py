# https://www.acmicpc.net/problem/11501
# greedy sliver 2

T = int(input())

for t in range(T):
  n = int(input())
  arr = list(map(int, input().split()))
  
  revArr = arr[::-1]
  cost = revArr[0]
  ans = 0

  for i in range(1, len(revArr)):
    if cost < revArr[i]:
      cost = revArr[i]
    else:
      ans += (cost - revArr[i])

  print(ans)