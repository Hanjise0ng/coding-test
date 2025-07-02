# https://www.acmicpc.net/problem/1543
# greedy sliver 5

doc = input()
word = input()
idx = 0
cnt = 0

while idx < len(doc):
    if doc[idx : idx + len(word)] == word:
        cnt += 1
        idx += len(word)
    else:
        idx  += 1

print(cnt)