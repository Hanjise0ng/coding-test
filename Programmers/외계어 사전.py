# permutations level 0

from itertools import permutations

def solution(spell, dic):
    answer = 2

    arr = list(permutations(spell, len(spell)))

    for a in arr:
        text = ''
        for idx in range(len(a)):
            text += a[idx]

        if text in dic:
            answer = 1

    return answer