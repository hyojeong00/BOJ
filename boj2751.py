import sys
n=int(sys.stdin.readline().strip())
li=[]
for i in range(n):
    a=int(sys.stdin.readline().strip())
    li.append(a)
li.sort()
for i in li:
    print(i)