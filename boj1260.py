from collections import deque

# 깊이 우선
def dfs(v):
    print(v, end = ' ')
    visited[v] = True
    for e in adj[v]:
        if not(visited[e]):
            dfs(e)

# 너비 우선
def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not (visited[v]):
            visited[v] = True
            print(v, end = ' ')
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)

n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)

# def dfs(graph, root):  #깊이 우선
#     visited = []
#     stack = [root]
    
#     while stack:
#         n = stack.pop()
#         if n not in visited:
#             visited.append(n)
#             if n in graph:
#                 temp = list(set(graph[n])-set(visited))
#                 temp.sort(reverse=True)
#                 stack += temp
#     return ' '.join(str(i) for i in visited)

# def bfs(graph, root):
#     visited = []
#     queue = deque([root])
    
#     while queue:
#         n = queue.popleft()
#         if n not in visited:
#             visited.append(n)
#             if n in graph:
#                 temp = list(set(graph[n])-set(visited))
#                 temp.sort()
#                 queue += temp
#     return ' '.join(str(i) for i in visited)

# graph = {}
# n = input().split()
# node, edge, start = [int(i) for i in n]

# for i in range(edge):
#     edge_info = input().split()
#     n1, n2 = [int(j) for j in edge_info]
#     if n1 not in graph:
#         graph[n1]=[n2]
#     elif n2 not in graph[n1]:
#         graph[n1].append(n2)
        
#     if n2 not in graph:
#         graph[n2] = [n1]
#     elif n1 not in graph[n2]:
#         graph[n2].append(n1)
        
# print(dfs(graph,start))
# print(bfs(graph,start))