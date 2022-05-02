lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]

def solution(lottos, win_nums):
    cnt = 0
    temp_cnt = 0
    for n in lottos:
        if n != 0 and n in win_nums:
            cnt += 1
        elif n == 0:
            temp_cnt += 1

    if not cnt and not temp_cnt:
        best = 6
    else:
        best = 7 - (cnt + temp_cnt)

    if cnt == 0:
        worst = 6
    else:
        worst = 7 - cnt

    return [best, worst]