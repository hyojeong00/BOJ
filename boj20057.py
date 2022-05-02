from collections import deque
from pprint import pprint
import math
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]  # 좌하우상
dy = [-1, 0, 1, 0]

dir = [[[-1,-1,0.1], [-1,0,0.07], [-1,1,0.01],[1,-1,0.1],[1,0,0.07],[1,1,0.01],[-2,0,0.02],[2,0,0.02],[0,-2,0.05],[0,-1,0.55]],
        [[-1,1,0.01],[0,1,0.07],[1,1,0.1],[-1,-1,0.01],[0,-1,0.07],[1,-1,0.1],[0,2,0.02],[0,-2,0.02],[2,0,0.05],[1,0,0.55]],
        [[-1,-1,0.01], [-1,0,0.07], [-1,1,0.1],[1,-1,0.01],[1,0,0.07],[1,1,0.1],[-2,0,0.02],[2,0,0.02],[0,2,0.05],[0,1,0.55]],
        [[-1,1,0.1],[0,1,0.07],[1,1,0.01],[-1,-1,0.1],[0,-1,0.07],[1,-1,0.01],[0,2,0.02],[0,-2,0.02],[-2,0,0.05],[-1,0,0.55]]]
# ㅜㅠ,,,좌하우상

q = deque()
x = N//2
y = N//2

for i in range(1,N):
    if i == N-1:
        for _ in range(3):
            q.append(i)
    else:
        for _ in range(2):
            q.append(i)

result = 0
for i in range(len(q)):
    for j in range(q[i]):
        nx = x + dx[i % 4]
        ny = y + dy[i % 4]
        if 0 <= x < N and 0<= y < N:
            for k in range(10):
                nnx = nx + dir[i % 4][k][0]
                nny = ny + dir[i % 4][k][1]
                if 0 <= nnx < N and 0 <= nny < N:
                    arr[nnx][nny] += arr[nx][ny]*dir[i%4][k][2]
                else:
                    result += arr[nx][ny]*dir[i%4][k][2]
            arr[nx][ny] = 0
            x, y = nx, ny
pprint(math.trunc(result))
