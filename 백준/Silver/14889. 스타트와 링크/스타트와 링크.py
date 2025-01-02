def cal(alst,blst):
    asum = bsum = 0
    for i in range(M):
        for j in range(M):
            asum += arr[alst[i]][alst[j]]
            bsum += arr[blst[i]][blst[j]]
    return abs(asum - bsum)

def dfs(n, alst,blst):
    global ans
    if n==N:
        if len(alst)==len(blst):
            ans = min(ans, cal(alst,blst))
        return

    dfs(n+1, alst+[n], blst)# A팀 선택
    dfs(n+1, alst, blst+[n])# B팀 선택

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

M = N//2

ans = 100*N*N

dfs(0, [], [])

print(ans)
