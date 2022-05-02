N = int(input())
parents = [0 for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    parents[b] = a

M = int(input())
for j in range(M):
    x, y = map(int, input().split())
    p_x = [x]
    p_y = [y]
    while parents[x]:
        p_x.append(parents[x])
        x = parents[x]
    while parents[y]:
        p_y.append(parents[y])
        y = parents[y]
    print(p_x,p_y)