from collections import deque
# 세로선 개수, 가로선 개수(실제), 가로선 놓을 수 있는 개수(가능)
import sys
input = sys.stdin.readline
N, M, H = map(int,input().split())

ladder = [[0] * (N+2) for _ in range(H+2)]

for _ in range(M):
    a, b = map(int,input().split())
    ladder[a][b] = 1

answer = 4 # INF
################## 입력 받기##################

################## 함수 #####################
def is_valid():
    for start in range(1,N+1):
        k = start
        for h in range(1,H+1):
            if ladder[h][k]:
                k+=1
            elif ladder[h][k-1]:
                k -=1
        if k!=start:
            return False
    return True

def dfs(count, x, y):
    global answer
    if count >= answer:
        return
    if is_valid():
        answer = count
        return
    if count == 3:
        return

    for i in range(x,H+1): # i는 행높이
        for j in range(1,N):
            if ladder[i][j] == ladder[i][j-1] == ladder[i][j+1]== 0:
                ladder[i][j] = 1
                dfs(count+1, i, j+2)
                ladder[i][j] = 0
################## 함수 #####################
dfs(0,1,1) # 시작 지점과 추가한 개수
print(answer if answer < 4 else -1)