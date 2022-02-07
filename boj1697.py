import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())

max = 100000
distance = [0] * 100001

def bfs():
    q = deque()
    q.append(n) # 현재 위치 삽입
    while q:
        x = q.popleft()
        if x == k:
            print(distance[x])
            break
        
        for j in (x-1,x+1,x*2):
            if 0 <= j <= max and not distance[j]:
                distance[j] = distance[x]+1
                q.append(j)

bfs()
