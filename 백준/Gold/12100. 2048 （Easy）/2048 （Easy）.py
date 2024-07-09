from collections import deque
n = int(input())
max_result = 0
result = []
# count =0 
## bfs -> 백트래킹
## 스택 -> 2048 합치기

def maze_sum(idx:int,maze) -> list:
    # 위로합치는 경우, y값이 늘어나는 순서로 합치기
    # 일단 넣고, 제일 마지막에 계산하여 반환
    new_maze=[]
    if(idx==0):
        # print("위")
        for i in range(n): # x값 -> 임의로
            dq = deque()
            for j in range(n-1,-1,-1): # y값 -> 높->낮게
                if(maze[i][j]):
                    dq.append(maze[i][j])
            new_maze.append(stack(dq))
    elif(idx==1):
        # print("아래")
        for i in range(n): # x값 -> 임의로
            dq = deque()
            for j in range(n): # y값 -> 낮->높
                if(maze[i][j]):
                    dq.append(maze[i][j])
            new_maze.append(stack(dq))
    elif(idx==2):
        # print("왼")
        for j in range(n): # y값 -> 임의로
            dq = deque()
            for i in range(n-1,-1,-1): # x값 -> 낮아지게
                if(maze[i][j]):
                    dq.append(maze[i][j])
            new_maze.append(stack(dq))
    else:
        # print("오")
        for j in range(n): # y 값 -> 임의로
            dq = deque()
            for i in range(n): # x값 -> 높아지게
                if(maze[i][j]):
                    dq.append(maze[i][j])
            new_maze.append(stack(dq))
    return new_maze

def stack(dq:deque)->list:
    result = []
    while(dq):
        try:
            if(dq[0] == dq[1]):
                tmp = dq.popleft()
                dq.popleft()
                result.append(tmp*2)
            else:
                result.append(dq.popleft())
        except:
            result.append(dq.popleft())
    length = len(result)
    return result + [0]*(n-length)

def bfs(lst:list):
    global max_result
    global result
    # global count
    dq = deque()
    dq.append((lst,0))
    while(dq):
        tmp, depth = dq.popleft()
        if(depth==5):
            # count +=1
            result.append(max(map(max,tmp)))
            continue
        for i in range(4):
            temp = maze_sum(i,tmp)
            dq.append((temp, depth+1))
    


maze = [list(map(int, input().split())) for _ in range(n)]

bfs(maze)
print(max(result))
# print(count)
# 시작은 [0,0,0,0,0], score