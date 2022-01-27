def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
def lcm(a,b):
    return (a * b) // gcd(a,b)
    
'''
갑자 구하기
k년일 경우 
k = 10 * i + 나머지1(x) == 12 * j + 나머지2(y)
즉, 나머지1(x) + 10*i 를 12로 나누었을 때, 나머지2(y)와 같아야 함 
'''
# 결국 x+(m*i) 를 n으로 나눠준 나머지가 y와 같아야 함
# ==> x에 y를 빼주고 n으로 나누어떨어지면 정답
# 15번째 예시 <5,3>
#  5 % 12 = 5
#  15 % 12 = 3  -> 15번째 해
# --------------------------
# 5 -3 % 12 = 2
# 15 -3 % 12 = 2  -> 15번째 해

def cal(m,n,x,y):
    lcm_ = lcm(m,n)  # 최소 공배수, 멸망의 날(60갑자 참고)
    while x < lcm_:  # 멸망의 날 전까지
        if (x - y) % n == 0:  # x에 y를 빼주고 n으로 나누어떨어지면 정답
            return x
        x += m  # x에 계속 m을 더해줌 (위 주석에서 i)
    return -1

test = int(input())
for _ in range(test):
    m, n, x, y = map(int,input().split())
    print(cal(m,n,x,y))