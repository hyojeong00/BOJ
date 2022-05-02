
def distance(now,target):
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    n = []
    t = []
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == now:
                n = [i,j]
            elif keypad[i][j] == target:
                t = [i,j]
    return abs(n[0]-t[0])+abs(n[1]-t[1])

def solution(numbers,hand):
    answer = ''
    now_L = '*'
    now_R = '#'
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            now_L = num
        elif num in [3, 6, 9]:
            answer += 'R'
            now_R = num
        else:
            L_cnt = distance(now_L,num)
            R_cnt = distance(now_R,num)
            if L_cnt > R_cnt:
                answer += 'R'
                now_R = num
            elif L_cnt < R_cnt:
                answer += 'L'
                now_L = num
            else:
                if hand == 'right':
                    answer += 'R'
                    now_R = num
                else:
                    answer += 'L'
                    now_L = num
    return(answer)


numbers = [4, 5, 0]
hand = "right"
print(solution(numbers, hand))