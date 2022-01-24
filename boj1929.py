import sys
input = sys.stdin.readline

def prime(number):  #소수판정
    for i in range(2, int(number**0.5)+1):
        if number % i ==0:
            return False
    return True

m, n = map(int,input().split())
for i in range(m,n+1):
    if i == 1:
        pass
    elif prime(i)==True:
        print(i)