import sys
input = sys.stdin.readline

def prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i ==0:
            return False
    return True

n = int(input().rstrip())

primes = list(map(int, input().split()))
cnt = 0
for number in primes:
    if prime(number)==True:
        cnt+=1

print(cnt)
