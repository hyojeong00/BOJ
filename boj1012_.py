from collections import deque

def bfs(a, b):
    global visited, arr
    q = deque()

    q.append([a,b])
    visited[a][b] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] == 1:
                q.append([nx,ny])
                visited[nx][ny] = True

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())  # 가로 길이, 세로 길이, 배추 위치 수
    arr = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())  # 가로, 세로로 들어옴 ㅜㅜ
        arr[b][a] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                result += 1
    print(result)