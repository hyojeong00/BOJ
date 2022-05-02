from collections import deque

idx = 1
while True:
    N = int(input())
    if N == 0:
        exit()

    arr = [list(map(int, input().split())) for _ in range(N)]
    cost = [[999]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    q = deque([[0,0]])
    cost[0][0] = arr[0][0]
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        visited[0][0] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if cost[nx][ny] > cost[x][y] + arr[nx][ny]:
                    cost[nx][ny] = cost[x][y] + arr[nx][ny]
                    q.append([nx,ny])

    print(f'Problem {idx}: {cost[N-1][N-1]}')
    idx += 1