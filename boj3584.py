import sys

T = int(sys.stdin.readline())
for case in range(T):
    N = int(sys.stdin.readline())
    parents = [0 for _ in range(N + 1)]
    for i in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        parents[b] = a

    x, y = map(int, sys.stdin.readline().split())
    p_x = [x]
    p_y = [y]
    # x의 조상들을 쭉  [3, 16, 10, 4, 8]
    while parents[x]:
        p_x.append(parents[x])
        x = parents[x]
    # y의 조상들을 쭉  [2, 10, 4, 8]
    while parents[y]:
        p_y.append(parents[y])
        y = parents[y]

    # 마지막 값이 root이므로 끝에서 부터 시작
    x_idx = len(p_x) - 1
    y_idx = len(p_y) - 1
    while p_x[x_idx] == p_y[y_idx]:  #두개가 달라지면 그 전에 idx가 값
        x_idx -= 1
        y_idx -= 1

    print(p_x[x_idx + 1])