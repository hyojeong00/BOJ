def dfs(graph, start_node):  #깊이 우선 탐색
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()  #시작노드부터 하나씩
        if node not in visited:  # 해당 노드가 아직 방문한 노드가 아니라면
            visited.append(node)  # 방문
            need_visit.extend(graph[node])  
    return visited

def bfs(graph, start_node):  # 너비 우선 탐색
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    cnt = 0

    while need_visit:
        node = need_visit.pop(0) # 여기만 다름
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

# graph = dict()

# graph['A'] = ['B', 'C']
# graph['B'] = ['A', 'D']
# graph['C'] = ['A', 'G', 'H', 'I']
# graph['D'] = ['B', 'E', 'F']
# graph['E'] = ['D']
# graph['F'] = ['D']
# graph['G'] = ['C']
# graph['H'] = ['C']
# graph['I'] = ['C', 'J']
# graph['J'] = ['I']

# print(dfs(graph,'A'))
# print(bfs(graph, 'A'))

graph = {}
node, edge, start = map(int, input().split())
