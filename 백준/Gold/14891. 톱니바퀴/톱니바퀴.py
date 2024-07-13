# 톱니바퀴 9시 3시 중요
# 9시는 2, 3시는 6
# 극이 같으면 반대방향, 극이 다른면 같은 방향으로 회전

from collections import deque
a = [list(map(int,input())) for _ in range(4)] 

n = int(input())
# n극 0 s극 1

nxt = [1,-1]
def turn(idx,direct): # 회전
    # print(idx,direct)
    if direct == 1:
        a[idx] = [a[idx][7]] + a[idx][:7]
    else:
        a[idx] =  a[idx][1:] + [a[idx][0]]



def is_chain_turn(idx, next_idx):
    if( idx < next_idx):# 진행 방향이 오른쪽
        if a[idx][2] != a[next_idx][6]: # 극이 다름 -> 역방향 회전    
            return True
        # 극이 같음 -> 회전 x
    elif( idx > next_idx):# 진행 방향이 왼쪽
        if a[idx][6] != a[next_idx][2]:
            return True
    return False

def bfs(idx,direct):
    visited = [0]*4
    visited[idx] = 1
    dq = deque()
    dq_simul = deque()
    dq.append((idx,direct))
    while(dq):
        tmp,tmp_d = dq.popleft()
        # turn(tmp,tmp_d)
        dq_simul.append((tmp,tmp_d))
        for i in range(2):
            nx = tmp + nxt[i]
            if(0<=nx<4):
                if(visited[nx] == 0 and is_chain_turn(tmp,nx)):
                    visited[nx] = 1
                    dq.append((nx,tmp_d*(-1)))  
    while(dq_simul):
        tmp,tmp_d = dq_simul.popleft()
        turn(tmp,tmp_d)
                         


for _ in range(n):
    idx, direct = map(int, input().split(" "))

    bfs(idx-1,direct)


result = 0
for i in range(4):
    result += a[i][0]*2**i

print(result)