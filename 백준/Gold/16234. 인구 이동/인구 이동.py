import sys
import math
from collections import deque
input = sys.stdin.readline

N, L, R = map(int,input().split())
arr = []
for i in range(N):
    tmp = list(map(int,input().split()))
    arr.append(tmp)

answer = 0
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def check(a,b):
    if R >= abs(a-b) >= L:
        return True
    return False

def range_check(x,y):
    if N > x >=0 and N > y >= 0:
        return True
    return False

def dfs(x,y):
    population = 0
    dq = deque([(x,y)])
    country_list = []
    while dq:
        x,y = dq.popleft()
        country_list.append((x,y)) # 호출자에서 값을 업데이트할때 사용.
        population += arr[y][x]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if range_check(nx, ny) and check(arr[ny][nx], arr[y][x]) and not visited[ny][nx]:
                visited[ny][nx] = True
                dq.append((nx,ny))
    return population, country_list

while True:
    visited = [[False] * N for _ in range(N)]
    move_list = [] # 여기에는 (r,c) 형태를 저장
    for i in range(N):
        for j in range(N):
            if not visited[j][i]:
                visited[j][i] = True
                population, count_lst = dfs(i,j)
                if len(count_lst) > 1:
                    move_list.append((population, count_lst))

    if move_list:
        answer += 1
        for pop, count_lst in move_list:
            avg = math.floor(pop / len(count_lst))
            for x,y in count_lst:
                arr[y][x] = avg
    else: break

print(answer)