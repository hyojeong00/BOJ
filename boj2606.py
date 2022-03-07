from collections import deque


def bfs(graph, start):
    visited = []
    q = deque([start])

    while q:
        n = q.popleft()
        if n not in visited:
            visited.append(n)
            q.extend(graph[n])
    return len(visited) - 1


n = int(input())  # 컴퓨터 수
m = int(input())  # 연결된 컴퓨터 번호 쌍

graph = {}
for i in range(m):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = [b]
    elif b not in graph[a]:
        graph[a].append(b)

    if b not in graph:
        graph[b] = [a]
    elif a not in graph[b]:
        graph[b].append(a)
print(graph)
print(bfs(graph, 1))