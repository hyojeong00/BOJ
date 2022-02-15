import sys
input = sys.stdin.readline

x = input().rstrip()
y = input().rstrip()

dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]  # 0집합 포함

for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
        if x[i-1] == y[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])  # 좌, 상 중 큰 것

#print(dp)
print(dp[len(x)][len(y)])