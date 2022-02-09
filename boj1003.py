zero = [0] * 101
one = [0] * 101

zero[1], one[1] = 1, 0
zero[2], one[2] = 0, 1

for idx in range(3,101):
    zero[idx] = zero[idx-1] + zero[idx-2]
    one[idx] = one[idx-1] + one[idx-2]
    
T = int(input())
for case in range(T):
    num = int(input())
    print(zero[num+1], one[num+1])  #인덱스값이라 +1