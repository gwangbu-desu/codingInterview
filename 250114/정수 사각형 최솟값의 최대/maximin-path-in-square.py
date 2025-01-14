n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[1000000]*n for _ in range(n)]


dp[0][0] = arr[0][0]

for i in range(1,n):
    if dp[i-1][0] != 0:
        dp[i][0] = min(dp[i-1][0],arr[i][0])
    if dp[0][i-1] !=0:
        dp[0][i] = min(dp[0][i-1], arr[0][i])

for i in range(n):
    for j in range(n):
        a=min(dp[i-1][j], arr[i][j])
        b=min(dp[i][j-1], arr[i][j])
        dp[i][j] = max(a,b)

print(dp[n-1][n-1])