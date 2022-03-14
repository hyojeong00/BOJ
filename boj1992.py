from sys import stdin
input = stdin.readline

n = int(input())
video = [list(map(int,input().rstrip())) for _ in range(n)]
ans = []

def sum1(x, y, n):
    sum = 0
    for j in range(n):
        for i in range(n):
            sum += video[y+j][x+i]
    if sum == n*n or sum == 0:
        return True
    else:
        return False

def zip(x, y, n):
    if n == 1:
        if video[y][x] == 0:
            ans.append('0')
            return 0
        else:
            ans.append('1')
            return 0
    else:
        if sum1(x, y, n):
            if video[y][x] == 0:
                ans.append('0')
                return 0
            else:
                ans.append('1')
                return 0
        else:
            m = n//2
            ans.append('(')
            zip(x, y, m)
            zip(x + m, y, m)
            zip(x, y+m, m)
            zip(x+m, y+m, m)
            ans.append(')')
            return 0

zip(0, 0, n)
for letter in ans:
    print(letter,end='')