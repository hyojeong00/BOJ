import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())  #강의 갯수 n

study = []  # 강의
for x in range(n) :
  start, end = map(int, input().split())
  study.append([start, end])  #시작시간, 끝나는시간 넣어주기

# study.sort()  #정렬
# study=sorted(study, key=lambda x : (x[0],x[1])) 
# print(study)
study=sorted(study, key=lambda x : x[0])  #시작시간으로 정렬한 후
study=sorted(study, key=lambda x : x[1])  #끝시간으로 정렬
#print(study)
#print(study)

ends=0
cnt=0
for i,j in study:
  if i >= ends:  # 시작 시간이 끝나는 시간보다 더 크면
    cnt += 1  # 카운트+1
    ends = j

print(cnt)
