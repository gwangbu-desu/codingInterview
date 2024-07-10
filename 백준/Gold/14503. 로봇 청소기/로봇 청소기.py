n,m=map(int,input().split(" "))

r,c,d = map(int,input().split(" "))

maze = [list(map(int,input().split(" "))) for _ in range(n)]
nx = 0
ny = 0
dx = [-1,0,1,0] # 북, 동, 남, 서 -> 0,1,2,3
dy = [0,1,0,-1] # 반시계? 북, 서, 남, 동 -> 0,3,2,1
rotate = [0,3,2,1] # 반시계? 북, 서, 남, 동 -> 0,3,2,1
def clean(r,c,direction):
    if(maze[r][c] == 0):
        maze[r][c] = 2
    flag = 0
    for i in rotate:
        nx = r + dx[i]
        ny = c + dy[i]
        if (0<=nx<n and 0<=ny<m):
            if(maze[nx][ny]==1):
                continue
            if(maze[nx][ny]==0):
                flag = 1
    if(flag == 0): ## 현재 주위 4칸이 청소할곳이 없으면 후진
        nx = r - dx[direction]
        ny = c - dy[direction]
        if(maze[nx][ny] == 1):
            return
        clean(nx,ny,direction)
    else: ## 청소할 곳이 있다면 반시계 방향으로 돌기 만약 앞이 청소되지 않았다면 한 칸 전진
        # 현재 방향이 rotate의 몇번째 인덱스인지 구하기
        idx = rotate.index(direction)

        for i in range(1,5):
            direction = rotate[(idx+i)%4]
            nx = r + dx[direction]
            ny = c + dy[direction]
            if(0<=nx<n and 0<=ny<m):
                if maze[nx][ny] == 0:
                    clean(nx,ny,direction)
                    break
        

clean(r,c,d)

# maze.count(2)
result = 0
for i in maze:
    result += i.count(2)
print(result)