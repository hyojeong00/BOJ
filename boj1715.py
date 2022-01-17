import sys
import heapq
input=sys.stdin.readline

n=int(input().rstrip())  #n개
a=[]
for i in range(n):
    b=int(input().rstrip())  #n개의 숫자를 받아옴
    a.append(b)
    
heapq.heapify(a)  #heapq

result=0
for i in range(n-1): #n-1번의 연산
    temp=heapq.heappop(a)  #가장 작은 수
    temp2=heapq.heappop(a)  #그 다음 작은 수
    
    temp_sum=temp+temp2  #더해주기
    result+=temp_sum  #result에 저장
    heapq.heappush(a,temp_sum)  
    #print(a)
    
#print(sum(a))
print(result)