import sys
input=sys.stdin.readline

n = int(input())

for i in range(n):
  li=list(map(int,input().split()))
  li=sorted(li,reverse=True)
  print(li[2])