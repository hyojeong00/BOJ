import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())  #강의 갯수 n

study = []  # 강의
for x in range(n) :
  start, end = map(int, input().split())
  study.append([start, end])  #시작시간, 끝나는시간 넣어주기

study.sort()  #정렬
#print(study)

rooms = []
heapq.heappush(rooms, study[0][1])  # 가장 첫 수업의 끝나는 시간을 넣어줌

for y in range(1,n):  # 첫 요소는 썼으니 1부터 시작
  if study[y][0] < rooms[0] : # 시작 시간이 현재 회의 끝나는 시간보다 빠르면
    heapq.heappush(rooms, study[y][1])  #끝나는 시간을 넣어줌(회의실+1)
  else:  # 시작 시간이 현재 회의 끝나는 시간보다 늦으면(이어서 쓸 수 있으면)
    heapq.heappop(rooms)  #이어하는 강의의 끝나는 시간으로 push
    heapq.heappush(rooms, study[y][1])

print(len(rooms))