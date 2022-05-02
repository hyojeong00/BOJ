from collections import deque
N = int(input())
graph = [[] for _ in range(N+1)]
# maximum = []
for _ in range(N-1):
    start, end, value = map(int,input().split())
    graph[start].append([end, value])
    graph[end].append([start, value])  #  무방향그래프처럼 그려주기
#     if not maximum:
#         maximum = [start, end, value]
#     elif maximum[2] < value:
#         maximum = [start, end, value]
# # max의 end에서 bfs를 시작하자! => 아님 ㅠㅠ
# maximum = maximum[1]


visited = [-999] * (N+1)
visited[1] = 0
q = deque()
q.append(1)

while q:
    now = q.popleft()
    for node, value in graph[now]:
        if visited[node] == -999:
            visited[node] = visited[now] + value
            q.append(node)



x = visited.index(max(visited))
visited = [-999] * (N+1)
visited[x] = 0
q = deque()
q.append(x)

while q:
    now = q.popleft()
    for node, value in graph[now]:
        if visited[node] == -999:
            visited[node] = visited[now] + value
            q.append(node)
print(max(visited))