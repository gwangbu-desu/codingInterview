import sys
import copy
sys.setrecursionlimit(10**6)
n=int(input())
arr = [list(map(int,input().split(" "))) for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def dfs(arr2,x,y,cost):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and arr2[nx][ny]>cost:
            arr2[nx][ny]=0
            dfs(arr2,nx,ny,cost)
        
result= 0 
for cost in range(max(map(max,arr))):
    count=0
    global cp
    cp=copy.deepcopy(arr)
    for i in range(n):
        for j in range(n):
            if(cp[i][j]>cost):
                dfs(cp,i,j,cost)
                count+=1
    result=max(result,count)
print(result)