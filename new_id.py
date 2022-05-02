new_id = "abcdefghijklmn.p"
def solution(new_id):
    marks = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '[', '{', ']', '}', ':', '?', ',', '<', '>', '/']

    # 1단계
    new_id = new_id.lower()

    # 2단계 ...bat..y.abcdefghijklm
    for c in new_id:
        if c in marks:
            new_id = new_id.replace(c, '')

    # 3단계
    rec_id = ''
    for i in range(len(new_id)):
        if i != 0 and new_id[i-1] =='.' and new_id[i] == '.':
            continue
        rec_id += new_id[i]

    # 4단계
    if len(rec_id) > 0 and rec_id[0] == '.':
        rec_id = rec_id[1:]
    if len(rec_id) > 0 and rec_id[-1] == '.':
        rec_id = rec_id[:-1]

    # 5단계
    if rec_id == '':
        rec_id = 'a'

    # 6단계
    if len(rec_id) >= 16:
        rec_id = rec_id[:15]
        if rec_id[-1] == '.':
            rec_id = rec_id[:14]

    # 7단계
    if len(rec_id) <= 2:
        while len(rec_id) < 3:
            rec_id += rec_id[-1]

    return(rec_id)

print(solution(new_id))