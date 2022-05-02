def solving(start):
    distance[start] = 0

    for _ in range(N+1):
        idx = -1
        val = 99999
        for i in range(N+1):
            if not visited[i] and distance[i] < val:
                idx = i
                val = distance[i]
        visited[idx] = 1

        for i in range(N+1):
            if load[idx][i] and not visited[i]:
                if distance[idx] + load[idx][i] < distance[i]:
                    distance[i] = distance[idx] + load[idx][i]

T = int(input())
for case in range(1, T+1):
    N, E = map(int, input().split())  #연결지점 번호, 도로 개수
    arr = [list(map(int, input().split())) for _ in range(E)]

    load = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for start, end, w in arr:
        load[start][end] = w

    distance = [99999 for _ in range(N+1)]
    visited = [0] * (N+1)

    start = 0
    solving(start)

    print(f'#{case} {distance[N]}')