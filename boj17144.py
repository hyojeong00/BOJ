from pprint import pprint
from collections import deque
from copy import deepcopy
# 일단 확산시킨다
# 1. 큐에 공기청정기 좌표를 넣는다
# 2. 첫 루프는 위로 두번째 루프는 밑으로 돈다

R, C, T = map(int, input().split())  # 위치, T초
arr = [list(map(int, input().split())) for _ in range(R)]

q = deque()  # 공기청정기의 위치
pprint(arr)

for x in range(R):
    for y in range(C):
        if arr[x][y] == -1:
           q.append([x,y])


dx = [-1, 1, 0, 0]  # R  하, 상, 좌, 우
dy = [0, 0, -1, 1]  # column

def spreading(arr, R, C):
    spread = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            temp = arr[x][y] // 5
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != -1:
                    spread[nx][ny] += temp
                    cnt += 1
            arr[x][y] -= temp * cnt

    for i in range(R):
        for j in range(C):
            arr[i][j] += spread[i][j]


def clean(x1,x2):

    for i in range(x1-2, -1, -1):
        arr[i+1][0] = arr[i][0]
    for i in range(1, C):
        arr[0][i-1] = arr[0][i]
    for i in range(1, x1+1):
        arr[i-1][-1] = arr[i][-1]
    for i in range(C-2, 0, -1):
        arr[x1][i+1] = arr[x1][i]
    arr[x1][1] = 0

    for i in range(x2+2, R):
        arr[i-1][0] = arr[i][0]
    for i in range(1, C):
        arr[-1][i-1] = arr[-1][i]
    for i in range(R-2, x2-1, -1):
        arr[i+1][-1] = arr[i][-1]
    for i in range(C-2, 0, -1):
        arr[x2][i+1] = arr[x2][i]
    arr[x2][1] = 0



x1,y1 = q.pop()
x2,y2 = q.pop()
for _ in range(T):
    spreading(arr, R, C)
    clean(x1,x2)


pprint(arr)
result = 0
for i in range(R):
    result += sum(arr[i])

print(result)
