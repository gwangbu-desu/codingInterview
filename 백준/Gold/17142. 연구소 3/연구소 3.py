import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

N, M = map(int,input().split()) # 지도 크기, 바이러스 개수
arr = []
virus_locate = []
virus_time = dict()
visited = set()

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(N):
    tmp = list(map(int,input().split()))
    arr.append(tmp)
    for j in range(N):
        if tmp[j] == 2:
            virus_locate.append((i,j))
################### 입력
def check(i,j):
    if 0<=i <N and 0<=j <N:
        return True
    return False
def bfs(i,j):
    time_arr = deepcopy(arr)
    time_arr[i][j] = -1
    dq = deque([])
    dq.append((i,j))
    while dq:
        i, j = dq.popleft()
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if check(ni,nj) and (time_arr[ni][nj] == 0 or time_arr[ni][nj] == 2):
                time_arr[ni][nj] = time_arr[i][j] - 1 # 방문, 시간 표시(음수 인덱스)
                dq.append((ni,nj))
    return time_arr

answer = 10000
def cal_minimum(time_lst):
    global answer
    map_arr = [[None] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            times = [t[i][j] for t in time_lst if t[i][j] != 0]
            if arr[i][j] == 2:
                map_arr[i][j] = -1
            else:
                map_arr[i][j] = max(times, default = 0) # 음수를 넣었으므로 max로
    ans = 0
    for tmp in map_arr:
        for value in tmp:
            if value == 0:
                return
            ans = min(ans, value)
    if ans < 0:
        answer = min(answer, ans*(-1) -1 )


def dfs(locate_lst, idx):  # 백트래킹
    if len(locate_lst) == M:
        # 만약 visited에 있다면 바로 return
        # if locate_lst in visited:
        #     return
        # 이곳에서 최소시간 구하고, visited 에 추가
        map_arr = []
        for x, y in locate_lst:
            map_arr.append(virus_time[(x,y)])
        cal_minimum(map_arr)
        # visited.add(locate_lst)
        return
    if idx == len(virus_locate):
        return
    x,y = virus_locate[idx]
    dfs(locate_lst + [(x,y)], idx + 1)
    dfs(locate_lst, idx + 1)


for i,j in virus_locate:
    virus_time[(i,j)] = bfs(i,j) # 2차원 시간 배열 넣기

# 백트래킹으로 5C3 하기
dfs([],0)
print(answer if answer != 10000 else -1)