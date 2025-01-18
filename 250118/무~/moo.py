# s(t) = s(t-1) + m + o * (t+2) + s(t-1)

n = int(input())

dp = ["moo"]

def s(t):
    if t == 0:
        return dp[0]
    if dp[t]:
        return dp[t]
    else:
        dp[t] = s(t-1) + "m" + "o"*(t+2) + s(t-1)
        return dp[t]
count = 0
while True:
    dp.append("")
    s(count)
    if len(dp[count]) > n:
        break
    count+=1


print(dp[count][n-1])