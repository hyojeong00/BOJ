from collections import deque
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
def solution(places):
    result = [1] * 5
    for p in range(5):
        person = deque()
        for i in range(5):
            for j in range(5):
                if places[p][i][j] == 'P':
                    person.append([i,j])
        result[p] = bfs(person, places, p)
    return result


def bfs(person, places, p):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for _ in range(len(person)):
        q = deque()
        a, b = person.popleft()
        q.append([a,b])
        visited = [[0]*5 for _ in range(5)]
        visited[a][b] = 1

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if visited[x][y] > 2:
                    q = deque()
                    continue
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    if places[p][nx][ny] == 'P' and visited[x][y] < 3:
                        return 0  # 거리가 2 이하인데
                    elif places[p][nx][ny] == 'X':
                        continue
                    else:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx,ny])
                        # if visited[nx][ny] > 2:
                        #     q = deque()
    return 1

print(solution(places))

