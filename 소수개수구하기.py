def prime(number):  #소수 판정
    for i in range(2, int(number**0.5)+1):  # 루트(넘버) 만큼만 돌면됨
        if number % i == 0:
            return False
    return True

def transform(n, k):  # 진수 변환
    result = ''
    while n > 0:
        result += str(n % k) # 나머지더해서 거꾸로~
        n = n // k
    return result[::-1]

def solution(n, k):
    target = transform(n,k)
    targets = []
    answer = 0

    temp = ''
    for idx in range(len(target)):
        if target[idx] != '0':
            temp += target[idx]
        if temp and (target[idx] == '0' or idx == len(target)-1):  # temp가 있고 중간에 0나오거나 마지막이면
            targets.append(temp)
            temp = ''

    for t in targets:
        if t != '1' and prime(int(t)):
            answer += 1

    return answer

n = 110011
k = 10
print(solution(n,k))