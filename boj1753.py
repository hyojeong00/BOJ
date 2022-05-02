import heapq
import sys
input = sys.stdin.readline

def dijkstra(K):
    q = []
    heapq.heappush(q, [0,K])
    distance[K] = 0  # 시작점은 0
    while q:
        dis, now = heapq.heappop(q)
        if distance[now] < dis:
            continue
        for i in graph[now]: # 현재지점과 연결되어 있는 곳 확인
            cost = dis + i[1] # 가중치
            if cost < distance[i[0]]: # 더 작은비용으로 갈 수 있으면 바꿔주기
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])


V, E = map(int, input().split())  # 정점의 개수, 간선의 개수
K = int(input())  # 시작 정점 번호
graph = [[] for _ in range(V+1)]
distance = [999999] * (V+1)  # 거리를 저장해줄 배열, 못가는 부분은 999999`

for i in range(E):
    u, v, w = map(int, input().split())  # u -> v, 가중치 w
    graph[u].append([v, w])

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == 999999:
        print('INF')
    else:
        print(distance[i])