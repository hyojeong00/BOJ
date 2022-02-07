import sys
input = sys.stdin.readline

n = int(input().rstrip())
stack = []
result = []
cnt = 1

for i in range(n):  
    data = int(input().rstrip())
    while cnt <= data:   # 1부터 시작하는 수열, 입력데이터까지 삽입
        stack.append(cnt)
        cnt += 1
        result.append('+')
    if stack[-1] == data:  # 스택의 마지막이 입력데이터와 같을때 pop
        stack.pop()
        result.append('-')
    else:
        print('NO')    # 아니면 NO
        exit(0)

print('\n'.join(result))