import heapq
T = int(input())
for tc in range(T):
    N = int(input())
    energy = list(map(int, input().split()))
    heapq.heapify(energy)

    if N == 1:
        print(1)
    else:
        result = 1
        while len(energy) > 1:
            n1 = heapq.heappop(energy)
            n2 = heapq.heappop(energy)
            result *= n1 * n2
            heapq.heappush(energy, n1 * n2)

        print(result % 1000000007)


