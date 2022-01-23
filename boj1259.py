import sys
input = sys.stdin.readline

def pal(number):
    number = str(number)
    if len(number)<2:
        return print('yes')
    if number[0] != number[-1]:
        return print('no')
    return pal(number[1:-1])

while True:
    number = int(input().rstrip())
    if number == 0:
        break
    else:
        pal(number)