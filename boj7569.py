from collections import deque
from pprint import pprint

M, N, H = map(int, input().split())  # 가로 칸 수, 세로 칸 수, 쌓은거
# 최소 날짜 출력, 0이 하나라도 있으면 -1

tomato = [[list(input().split()) for _ in range(N)] for _ in range(H)]
# pprint(tomato)

q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == '1':
                tomato[i][j][k] = 1  # 숫자로 바꾸기
                q.append([i,j,k])

dh = [1, -1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

result = 1
while q:
    h, x, y = q.popleft()

    for i in range(6):
        nh = h + dh[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and tomato[nh][nx][ny] == '0':
            tomato[nh][nx][ny] = tomato[h][x][y] + 1  # 날짜 하루씩 더하기
            q.append([nh, nx, ny])
            if result < tomato[nh][nx][ny]:  # result 갱신
                result = tomato[nh][nx][ny]


for i in range(H):
    for j in range(N):
        if '0' in tomato[i][j]:
            print(-1)  # 0이 남아있으면 -1출력하고 탈출
            exit()

else:
    print(result-1)
