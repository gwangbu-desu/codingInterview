#import sys
#sys.stdin = open("input.txt", "r")
from collections import deque
T = int(input())
global arr
global visited
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    arr =  [ [0]*(N + 2)]+[[0]+ list(input()) +[0] for _ in range(N)] + [[0]*(N+2)]
    ans = 0
    newMap = [ [-1]*(N+2)] + [[-1] + [0]*N +[-1] for _ in range(N)] + [[-1]*(N+2)]
    visited = [ [1]*(N+2)] + [[1] + [0]*N +[1] for _ in range(N)] + [[1]*(N+2)]

    for i in range(1,N+2):
        for j in range(1,N+2):

            if arr[j][i] == "*":
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    try:
                        if arr[ny][nx] == '.':
                            newMap[ny][nx] += 1
                    except:
                        continue
    # print(newMap)
    for i in range(1, N + 2):
        for j in range(1, N + 2):
            if arr[j][i] == "." and not visited[j][i]:
                if newMap[j][i] == 0:
                    q= deque([(i,j)])
                    while(q):
                        x,y = q.popleft()
                        visited[y][x] = 1
                        for k in range(8):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if arr[ny][nx] == "." and not visited[ny][nx]:
                                visited[ny][nx] = 1
                                if not newMap[ny][nx]:
                                    q.append((nx, ny))
                    ans+=1
    # print(visited)
    for i in range (1,N+2):
        for j in range (1,N+2):
            if newMap[j][i] > 0 and not visited[j][i]:
                ans+=1
    print(f"#{test_case} {ans}")
    # ///////////////////////////////////////////////////////////////////////////////////

