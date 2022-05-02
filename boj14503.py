from collections import deque

N, M = map(int, input().split())  # 세로크기N, 가로크기 M
r, c, d = map(int, input().split())  # 좌표와 바라보는 방향
# d = 0;북쪽, 1;동쪽, 2;남쪽, 3;서쪽

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 북동남서
# direction = [[0, -1], [-1, 0], [0,1], [1 ,0]] # 북동남서에서의 왼쪽  -> 세칸 밀면 됨! +3
# 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
# 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
# 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.

q = deque()
result = 1
print(d)
while q:
    cx, cy, cd = q.pop()
    check = False
    for i in range(4):
        nd = (direction[cd] + 3) % 4
        print(nd)
