import sys
from pprint import pprint
sys.stdin = open('sample_input.txt','r')

def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += set(graph[n]) - set(visited)
    return visited

T = int(input())
for case in range(1, T+1):
    V, E = map(int, input().split())
    adj =[[0]*(V+1) for _ in range(V+1)]
    adjList = [[] for _ in range((V+1))]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
        adjList[n1].append(n2)
    S, G = map(int, input().split())

    if G in dfs(adjList, S):
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')