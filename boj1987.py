dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  # 상하좌우

def bfs(x, y):
    global result
    q = set()
    q.add((x,y,arr[x][y]))
    while q:
        x, y, step = q.pop()
        result = max(result, len(step))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx and nx < r and 0 <= ny and ny < C and arr[nx][ny] not in step):
                q.add((nx,ny, step+arr[nx][ny]))

r, C = map(int, input().split())
arr=[input() for _ in range(r)]

result = 0
bfs(0,0)
print(result)