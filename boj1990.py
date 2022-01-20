import sys
input=sys.stdin.readline

def pal(word):  #팰린드롬 판정
    if len(word)<2:
        return True
    if word[0] != word[-1]:
        return False
    return pal(word[1:-1])

def prime(number):
    for i in range(2, int(num**0.5)+1):
        if num % i ==0:
            return False
    return True

start, end = map(int,input().split())
if end > 10000000:
    end = 10000000
    
li=[]
for i in range(start,end+1):
    i=str(i)
    if pal(i)==True:
        li.append(int(i))

for num in li:
    if prime(num)==True:
        print(num)

print(-1)