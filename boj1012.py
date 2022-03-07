import sys
sys.setrecursionlimit(100000)
from pprint import pprint
from collections import deque

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())  # 가로 길이, 세로 길이, 배추 위치 수
    arr = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    q = deque()
    for _ in range(K):
        y, x = map(int, input().split())  # 가로, 세로로 들어옴 ㅜㅜ
        arr[x][y] = 1
        q.append([x,y])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = 0
    while q:
        i, j = q.popleft()
        if arr[i][j] and not visited[i][j]:
            visited[i][j] = True
            for i in range(4):
                nx = i + dx[i]
                ny = j + dy[i]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append([nx, ny])
    pprint(arr)
    pprint(visited)
