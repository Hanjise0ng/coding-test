N, A, B = map(int, input().split())
praise_onion, rebuke_onion = 1, 1
for i in range(N):
    praise_onion += A
    rebuke_onion += B
    if praise_onion < rebuke_onion:
        praise_onion, rebuke_onion = rebuke_onion, praise_onion
    if praise_onion == rebuke_onion:
        rebuke_onion -= 1

print(praise_onion, rebuke_onion)