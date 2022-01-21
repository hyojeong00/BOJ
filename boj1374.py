import sys
import heapq
input=sys.stdin.readline

n = int(input().rstrip())  # 강의 갯수

study = []
for _ in range(n):
    num, start, end = map(int, input().split())  # 강의번호, 시작시간, 끝시간
    study.append([start, end])  # 시작시간, 끝시간
    
study.sort()

rooms = []
heapq.heappush(rooms, study[0][1])  # 가장 처음 시작하는 강의를 넣어줌

for i in range(1, n):  # 첫 강의를 이미 넣었기때문에 1부터 인덱스 시작
    if study[i][0] < rooms[0]:  # 시작시간이 들어가있는것보다 작으면(빠르면)
        heapq.heappush(rooms, study[i][1])  # 힙에 새로 넣어줌
    else:  #시작시간보다 느리지 않으면
        heapq.heappop(rooms)  # 가장 작은 수를 pop하고
        heapq.heappush(rooms, study[i][1])  # 끝나는 시간을 넣어줌
        
print(len(rooms))