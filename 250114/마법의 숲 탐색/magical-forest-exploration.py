

dx=[-1,0,1,0]
dy=[0,1,0,-1]
golemEntry=set()
# 1은 벽
# 2,3,4,5,6 ... 는 골렘


r,c,k = map(int,input().split())
arr = [[1]+[0]*c+[1] for _ in range(r+3)] + [[1] * (c+2)]

golemList =[]
for i in range(k):
    cl,dl = map(int,input().split())
    golemList.append((cl,dl))

def draw(r,c, count,dr):
    global arr
    global golemEntry
    arr[r][c] = arr[r+1][c] = arr[r-1][c] = arr[r][c+1] = arr[r][c-1] = count
    golemEntry.add((r+dx[dr],c+dy[dr]))

result = 0
count = 1
for cj,dr in golemList:
    count += 1
    ci = 1
    rsetcj,rsetdr = cj,dr
    while True:
        if arr[ci+1][cj-1] + arr[ci+2][cj] + arr[ci+1][cj+1] == 0:
            ci += 1
            continue
        elif arr[ci-1][cj-1] + arr[ci+1][cj-1] + arr[ci][cj-2] + arr[ci+1][cj-2] + arr[ci+2][cj-1] == 0 :
            cj -= 1
            ci += 1
            dr  = (dr-1)%4
            continue
        elif arr[ci-1][cj+1] + arr[ci][cj+2] + arr[ci+1][cj+1] + arr[ci+2][cj+1] + arr[ci+1][cj+2] == 0:
            ci += 1
            dr = (dr + 1)%4
            cj += 1
            continue
        break
    if ci < 4:
        arr = [[1]+[0]*c+[1] for _ in range(r+3)] + [[1] * (c+2)]
        golemEntry = set()

    else:
        ## 여기서 골렘 표시
        draw(ci,cj,count,dr)
        ## 여기서 점수 계산
        dq = [(ci,cj)]
        score = 0
        visited = [[0] * (c + 2) for _ in range(r + 4)]
        while dq:
            ci,cj = dq.pop(0)
            for i in range(4):
                ni = ci + dx[i]
                nj = cj + dy[i]
                if visited[ni][nj]:
                    continue
                if arr[ni][nj] == arr[ci][cj] or ((ci,cj) in golemEntry and arr[ni][nj]>1):
                    dq.append((ni,nj))
                    visited[ni][nj] = 1
                    score = max(score,ni - 2)
        result += score
print(result)