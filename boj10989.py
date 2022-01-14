import sys
input=sys.stdin.readline

n=int(input().rstrip())

num=[0]*10001   #메모리제한, counting sort
for x in range(n):
  a=int(input().rstrip())
  num[a]+=1  #자리에 1을 더해줌


for i in range(1,10001):
  if num[i]!=0:  #0이 아닌것(수가 들어온 것들)
    for j in range(num[i]):  #개수만큼
      print(i)  #i를 프린트해줌