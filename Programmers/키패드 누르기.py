# implementation level 1

def solution(numbers, hand):
    answer = ''
    key_dict = {
        1: (0, 0),   2: (0, 1),   3: (0, 2),
        4: (1, 0),   5: (1, 1),   6: (1, 2),
        7: (2, 0),   8: (2, 1),   9: (2, 2),
        '*': (3, 0),   0: (3, 1), '#': (3, 2),
    }

    left, right = [1, 4, 7], [3, 6, 9]
    lhand, rhand = '*', '#' # 시작 위치

    for num in numbers:
        if num in left:
            answer += "L"
            lhand = num
        elif num in right:
            answer += "R"
            rhand = num
        else:
            curr = key_dict[num]
            lpos = key_dict[lhand]
            rpos = key_dict[rhand]

            ldist = abs(curr[0]-lpos[0]) + abs(curr[1]-lpos[1])
            rdist = abs(curr[0]-rpos[0]) + abs(curr[1]-rpos[1])

            if ldist < rdist:
                answer += "L"
                lhand = num
            elif ldist > rdist:
                answer += "R"
                rhand = num
            elif ldist == rdist:
                if hand == "left":
                    answer += "L"
                    lhand = num
                elif hand == "right":
                    answer += "R"
                    rhand = num

    return answer