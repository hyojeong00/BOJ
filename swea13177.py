def solving(start, end):
    q = []
    v = [10000000] * 1001
    q.append(start)
    v[start] = 0
    while q:
        cur = q.pop(0)
        for next, w in arr[cur]:
            if v[next] > v[cur] + w:
                q.append(next)
                v[next] = v[cur] + w
    return v[end]


T = int(input())
for case in range(1, T + 1):
    N, E = map(int, input().split())

    arr = [[] for _ in range(1001)]
    for _ in range(E):
        start, end, w = map(int, input().split())
        arr[start].append((end, w))
    ans = solving(0, N)
    print(f'#{case} {ans}')