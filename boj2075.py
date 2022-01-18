import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())  # n개의 수 받아오기
heap = []

for x in map(int,input().split()):  # 처음 n개만 저장
    heapq.heappush(heap,x)

for y in range(1,n):  # 그 뒤 부터는
  for z in map(int,input().split()):
    heapq.heappush(heap,z)  # 넣고
    heapq.heappop(heap)  # 가장 작은거 빼고

print(heapq.heappop(heap)) # 남은 것들 중 가장 작은것
