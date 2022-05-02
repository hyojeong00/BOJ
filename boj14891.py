from pprint import pprint
from collections import deque

def turn(n,d):
    global circle
    if d == 1:
        first = circle[n-1].pop()
        circle[n-1].appendleft(first)
    else:
        last = circle[n - 1].popleft()
        circle[n - 1].append(last)


# 오른쪽은 idx -1, 왼쪽으로갈때는 idx 나눠보자!
def l(n):  # 왼쪽으로간다
    global rot
    for i in range(n-2,-1,-1):
        if check[i]:
            rot[i] = direction[i]
        else:
            return


def r(n):  # 오른쪽으로간다
    global rot
    for i in range(n,4):
        if check[i-1]:
            rot[i] = direction[i]
        else:
            return


circle = []
for _ in range(4):
    temp = deque(list(input().replace('\n','')))
    circle.append(temp)

K = int(input())  # 회전 횟수
for _ in range(K):
    N, D = map(int, input().split())  # 톱니바퀴 번호, 회전 방향; 1 시계, -1 반시계  / 3 -1
    check = [False]*3  # true면 돌려야함 [True, True, False]
    direction = [0]*4
    for d in range(4):
        if (N % 2 == 0 and D == 1) or (N % 2 == 1 and D == -1):
            direction = [-1, 1, -1, 1]
            break
        else:
            direction = [1, -1, 1, -1]
            break

    for j in range(3):
        if circle[j][2] != circle[j+1][6]:
            check[j] = True

    turn(N,D)  # 돌려돌려
    rot = [0] * 4

    r(N)
    l(N)  #좌우를 보세요

    for j in range(4):
        if rot[j] != 0:
            turn(j+1, rot[j])

result = 0
for i in range(4):
    if circle[i][0] == '1':
        result += 2**i
print(result)

    # if N == 1:  # [True, True, False] / [1, -1, 1, -1] / [0,-1,1,0]
    #     for i in range(4):  # 2
    #         if check[i-1] and i != N-1:
    #             r[i] = direction[i]
    #         elif not check[i-1] and i != N-1:
    #             break
    #     for j in range(4):
    #         if r[j] != 0:
    #             turn(j+1, r[j])
    # elif N == 2:
    #     # 왼쪽부터 쫙돌기
    #     for i in range(4):
    #         if i == 0:
    #             if check[0]:
    #                 r[i] = direction[i]
    #         elif check[i-1] and i != N-1:
    #             r[i] = direction[i]
    #         elif not check[i - 1] and i != N - 1:
    #             break
    #     for j in range(4):
    #         if r[j] != 0:
    #             turn(j+1, r[j])
    # elif N == 3:
    #     # 뒤부터 돌기  [True, True, True] / [-1, 1, -1, 1]
    #     for i in range(3,-1,-1):  # i = 3 -> 네번째 톱니바퀴1
    #         if check[i-1] and i == 3:  # [-1,1,0,1]
    #             r[i] = direction[i]
    #         elif i == 2:
    #             continue
    #         elif check[i] and i != N-1:
    #             r[i] = direction[i]
    #         else:
    #             break
    #     for j in range(4):
    #         if r[j] != 0:
    #             turn(j+1, r[j])
    # elif N == 4:
    #     # 뒤부터 돌기
    #     for i in range(3,-1,-1):  # 2
    #         if i == 3:
    #             continue
    #         if check[i] and i != N-1:
    #             r[i] = direction[i]
    #         elif not check[i] and i != N - 1:
    #             break
    #     for j in range(4):
    #         if r[j] != 0:
    #             turn(j+1, r[j])
    #
    # for i in range(4):
    #     print(list(circle[i]))
    # print()
    # print(r)

# result = 0
# for i in range(4):
#     if circle[i][0] == '1':
#         result += 2**i
# print(result)

















    # if D == 1:  # 시계방향
    #     right(N)
    #     check[N-1] = 1
    # else:  # 반시계방향
    #     left(N)
    #     check[N-1] = -1
    #
    # if N == 1:  # 첫번째 톱니바퀴라면
    #     for j in range(1, 4):
    #         while circle[j-1][2] != circle[j][6]:
    #             if check[j-1] == 1:
    #                 left(j+1)
    #                 check[j] = -1
    #             elif check[j-1] == -1:
    #                 right(j+1)
    #                 check[j] = 1
    # if N == 2: # 두번째 톱니바퀴라면
    #     for j in range(4):
    #         if j < N-1:  # 첫번째 톱니바퀴
    #             while circle[j][2] != circle[N-1][6]:
    #                 if check[j+1] == 1:
    #                     left(j+1)
    #                     check[j] = -1
    #                 elif check[j+1] == -1:
    #                     right(j+1)
    #                     check[j] = 1
    #         if j > N-1: # 세네번째
    #             while circle[j-1][2] != circle[j][6]:
    #                 if check[j-1] == 1:
    #                     left(j+1)
    #                     check[j] = -1
    #                 elif check[j-1] == -1:
    #                     right(j+1)
    #                     check[j] = 1
    # if N == 3: # 세번째 톱니바퀴
    #     for j in range(3, -1, -1):
    #         if j > N-1:  # 네번째 톱니바퀴일 때
    #             while circle[N-1][2] != circle[j][6]:
    #                 if check[j-1] == 1:
    #                     left(j+1)
    #                     check[j] = -1
    #                 elif check[j-1] == -1:
    #                     right(j+1)
    #                     check[j] = 1
    #         if j < N-1:  # 두번째, 첫번째
    #             while circle[j+1][6] != circle[j][2]:
    #                 if check[j+1] == 1:
    #                     left(j+1)
    #                     check[j] = -1
    #                 elif check[j+1] == -1:
    #                     right(j+1)
    #                     check[j] = 1
    # if N == 4:
    #     for j in range(2, -1, -1):
    #         while circle[j+1][6] != circle[j][2]:
    #             if check[j+1] == 1:
    #                 left(j + 1)
    #                 check[j] = -1
    #             elif check[j+1] == -1:
    #                 right(j + 1)
    #                 check[j] = 1






