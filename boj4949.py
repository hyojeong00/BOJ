import sys
input = sys.stdin.readline

# 스택 활용
while True:
    words = input().rstrip()
    stack = []
    check = True  # 짝 맞는지 체크할 변수

    if words == '.':
        break  # . 이들어오면 while 탈출

    for word in words:
        if len(stack) == 0 and word in [')',']']:  # 스택이 비어있고, 닫는 괄호 들어오면
            check = False  # 체크 False
            break  # 루프 탈출 

        if word in ['(','[']:  # 열린 괄호면
            stack.append(word)  # 스택에 넣기

        elif word ==')':  # 닫는 소괄호고
            if stack[-1] =='(':  # 최상위 스택이 여는소괄호면
                stack.pop()  # 스택pop -> 짝 맞음
            elif stack[-1] == '[':  # 여는 대괄호면 짝이 안맞음
                check=False
                break

        elif word == ']':
            if stack[-1] == '[':
                stack.pop()
            elif stack[-1] == '(':
                check=False
                break



    if len(stack) == 0 and check == True:  # 스택이 비었고, 짝 체크 변수가 True면
        print('yes')
    else:
        print('no')




