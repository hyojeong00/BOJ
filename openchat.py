record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    answer = []
    user = {}
    for r in record:
        if r.startswith('Enter'):
            keyword, uid, name = r.split()
            user[uid] = name
        elif r.startswith('Change'):
            keyword, uid, name = r.split()
            user[uid] = name

    for r in record:
        if r.startswith('Enter'):
            keyword, uid, name = r.split()
            answer.append(f'{user[uid]}님이 들어왔습니다.')
        elif r.startswith('Leave'):
            keyword, uid = r.split()
            answer.append(f'{user[uid]}님이 나갔습니다.')
    return answer

print(solution(record))