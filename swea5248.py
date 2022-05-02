def solving(n):
    if X[n] != n:
        X[n] = solving(X[n])
    return X[n]


def solving2(a, b):
    a = solving(a)
    b = solving(b)
    X[b] = a


T = int(input())
for case in range(1, T+1):
    N, M = map(int, input().split())
    X = [n for n in range(N+1)]
    arr = list(map(int, input().split()))
    result = 0

    for i in range(0, len(arr), 2):
        if solving(arr[i]) == solving(arr[i+1]):
            continue
        solving2(arr[i], arr[i+1])

    for i in range(1, N + 1):
        if i == X[i]:
            result += 1

    print(f'#{case} {result}')