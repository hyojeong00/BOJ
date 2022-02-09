dp = [0] * 1001
dp[1] = 1  # 2*1 크기의 직사각형일 경우 2*1 타일 1개
dp[2] = 2  # 2*2 크기면 2개

for idx in range(3,1001):
    dp[idx] = dp[idx-1] + dp[idx-2]
print(dp[int(input())] % 10007)