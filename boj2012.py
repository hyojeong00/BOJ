import sys
input = sys.stdin.readline

N = int(input().rstrip())
rank = []

for _ in range(N):
    rank.append(int(input().rstrip()))

rank.sort()

result = 0
for i in range(1, N+1):
    result += abs(i - rank[i-1])

print(result)