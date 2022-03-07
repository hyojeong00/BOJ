from collections import deque

M, N = map(int, input().split())  # 가로 칸 수, 세로 칸 수
# 최소 날짜 출력, 0이 하나라도 있으면 -1

tomato = [list(input().split()) for _ in range(N)]


q = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == '1':
            tomato[i][j] = 1  # 숫자로 바꾸기
            q.append([i,j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


result = 1
while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == '0':
            tomato[nx][ny] = tomato[x][y] + 1  # 날짜 하루씩 더하기
            q.append([nx,ny])
            if result < tomato[nx][ny]:  # result 갱신
                result = tomato[nx][ny]

for i in range(N):
    if '0' in tomato[i]:
        print(-1)  # 0이 남아있으면 -1출력하고 탈출
        exit()

else:
    print(result-1)
