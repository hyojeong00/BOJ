from collections import deque


def bfs(a, b, v):
    global arr, result
    q = deque()

    q.append([a, b])
    v[a][b] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 델타배열 탐색
            if 0 <= nx < N and 0 <= ny < N and not v[nx][ny] and arr[nx][ny] == arr[a][b]:
                q.append([nx, ny])
                v[nx][ny] = True
    result += 1  # 한뭉탱이 완성


N = int(input())
arr = [list(input()) for _ in range(N)]

# NO 색맹-----------------------------------
visited = [[False] * N for _ in range(N)]
result = 0

# 전체 탐색하면서 not visited인것 -> bfs
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, visited)
print(result, end=' ')
# --------색맹 코드 --------------------------
gr_visited = [[False] * N for _ in range(N)]
# G를 그냥 R로 바꾸기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
result = 0
for i in range(N):
    for j in range(N):
        if not gr_visited[i][j]:
            bfs(i, j, gr_visited)
print(result)