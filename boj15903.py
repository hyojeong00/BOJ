import sys
import heapq
input=sys.stdin.readline

n,m = map(int,input().split())  #카드 개수 n, 합체 횟수 m
a = list(map(int,input().split()))
heapq.heapify(a) # 힙으로

for i in range(m):
    temp = heapq.heappop(a)  # 가장 작은 수 pop
    temp2 = heapq.heappop(a) # 그 다음 작은 수 pop

    temp_sum = temp + temp2 # 두 수 더하기
    heapq.heappush(a,temp_sum) # 두번 넣어주기
    heapq.heappush(a,temp_sum)

print(sum(a))