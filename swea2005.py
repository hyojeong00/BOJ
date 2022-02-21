from pprint import pprint
T = int(input())

for case in range(1, T+1):
    n = int(input())
    dp = [[0]+[0]*(2*n-1)+[0] for _ in range(n)]  # 2n-1개 만큼 칸을 만들기+테두리
    dp[0][(2*n+1)//2]=1
    
    for i in range(1,n): # 두번째 줄 부터
        for j in range(1,2*n): 
            if (n % 2 == 0) and (i % 2 == 1 and j % 2 == 1) or (i % 2 == 0 and j % 2 == 0):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            elif (n % 2 == 1) and (i % 2 == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    
    print(f'#{case}')
    for x in range(n):
        for y in range(2*n+1):
            if dp[x][y] != 0:
                print(dp[x][y], end = ' ')
        print()