import heapq

N = int(input())
lecture = [list(map(int, input().split())) for _ in range(N)]

lecture = sorted(lecture, key = lambda x: x[0], reverse=True)  # 돈 많이주는순
lecture = sorted(lecture, key = lambda x: x[1])  # 시간순 정렬


q = []
for money, day in lecture:
    heapq.heappush(q, money)
    if day < len(q):
        heapq.heappop(q)

print(sum(q))