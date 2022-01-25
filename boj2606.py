from collections import deque

def bfs(graph, root):
    visited = []
    queue = deque([root])
    
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            temp = list(set(graph[n])-set(visited))
            temp.sort()
            queue += temp
    return len(visited)-1

n = int(input()) # 컴퓨터 수
if n >100:
    quit()

m = int(input()) # 연결된 컴퓨터 번호 쌍

graph = {}  # 그래프 만들기
for i in range(m):
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)
        
print(bfs(graph,1))