# from itertools import permutations
#
# N, M = map(int, input().split())
# li = map(str, range(1, N+1))
#
# print('\n'.join(list(map(' '.join,permutations(li, M)))))

def back(x):
    if x == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return

    for i in range(N):
        if arr_[i] == 0:
            arr[x] = i + 1
            arr_[i] = 1
            back(x + 1)
            arr_[i] = 0

N, M = map(int, input().split())  # 1부터 N까지 중복없이 M개
arr = []
arr_ = []
for i in range(N):  # N개 만큼
    arr_.append(0)
for i in range(M):  # 결과
    arr.append(0)

back(0)