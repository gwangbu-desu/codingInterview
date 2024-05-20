import sys
sys.setrecursionlimit(10**6)

dp=[0]*5001
def dynamic(n):
        if n==0:
            return 1
        if n==1: return 0
        if n==2: return 3
        if dp[n]:
            return dp[n]
        dp[n] = 3* dynamic(n-2)
        for i in range(4,n+1,2):
            dp[n]+=2*dynamic(n-i)
        dp[n]%=1000000007
        return dp[n]

def solution(n):
    answer = 0
    
    answer = dynamic(n)
    return answer