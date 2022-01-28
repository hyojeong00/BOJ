n = int(input())
tower = list(map(int,input().split()))  # 탑의 높이 받아오기
towers = []
for tow in enumerate(tower):  # 인덱스와 함께 저장
    towers.append(list(tow))

stack = []
result= [0 for x in range(n)]  # 빈 리스트로 만들 경우 보다 큰 탑이 없는 경우 누락

for i in range(n):
    while stack:
        if stack[-1][1] > towers[i][1]:
            result[i] = stack[-1][0]+1
            break
        else:
            stack.pop()
    stack.append([i, towers[i][1]])  
    
for i in range(len(result)):
    print(result[i],end = ' ')