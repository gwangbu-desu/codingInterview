from collections import deque

n,m = map(int,input().split(" "))

maze = [list(input().rstrip()) for _ in range(n)]
visited = []
# 시간복잡도 = 200,000,000 번
# n,m = 10 이하
# 20,000,000 번 -> n^2*logn?

# bfs 사용 -> 빨강 파랑 동시 시행

# .은 이동가능, R은 O으로 들어가야됨. B는 들어가면안됨
# 공은 벽을 만날때까지 움직임
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def forward(x,y,i):
    cnt=0
    while(maze[x + dx[i]][y + dy[i]] != "#" and maze[x][y] != "O"):
        x = x + dx[i]
        y = y + dy[i]
        cnt +=1
    return x, y, cnt

def bfs(rx,ry,bx,by):
    dq = deque()
    tmp = (rx,ry,bx,by,1)
    dq.append(tmp)
    visited.append(tmp)
    nrx=nry=nbx=nby=0
    while(dq):
        rx,ry,bx,by,result = dq.popleft()
        if result > 10:
            break
        for i in range(4):
            nrx, nry, rcnt = forward(rx,ry,i)
            nbx, nby, bcnt = forward(bx,by,i)

            if maze[nbx][nby] == "O":
                continue
            if maze[nrx][nry] == "O":
                print(result)
                return
            
            if nrx == nbx and nry == nby:
                if rcnt < bcnt:
                    nbx -= dx[i]
                    nby -= dy[i]
                else:
                    nrx -= dx[i]
                    nry -= dy[i]
            
            if (nrx,nry,nbx,nby) not in visited:
                visited.append((nrx,nry,nbx,nby))
                dq.append((nrx,nry,nbx,nby,result+1))
    print(-1)

rx=ry=bx=by=0
for i in range(n):
    for j in range(m):
        if maze[i][j] == "R":
            rx = i
            ry = j
        if maze[i][j] == "B":
            bx = i
            by = j

bfs(rx,ry,bx,by)
