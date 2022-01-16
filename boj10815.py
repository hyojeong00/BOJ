import sys
input=sys.stdin.readline

n=int(input().rstrip())  #상근이가 가지고 있는 카드 갯수
nums=set(map(int,input().split()))  #상근이가 가지고 있는 카드

m=int(input().rstrip())  #구해야 할 숫자의 개수
nums_m=list(map(int,input().split()))  #구해야 할 수

for i in nums_m:  #nums_m들 중에서(구해야 할 수)
  if i in nums:  #nums에 포함되어있으면(가지고 있는 수)
    print(1,end=' ') #1을 출력
  else:
    print(0,end=' ') #아니면 0 출력