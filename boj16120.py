text = input()
if text == 'P' or text == 'PPAP':  # P나 PPAP면 PPAP문자
    print('PPAP')
else:
    stack = []
    PPAP = ['P','P','A','P']  # 비교용
    for cha in text:
        stack.append(cha)
        if stack[-4:] == PPAP:  # PPAP가 완성되면 P만 두고 뽑기
            stack.pop()
            stack.pop()
            stack.pop()
    if stack == PPAP or stack == ['P']:
        print('PPAP')
    else:
        print('NP')