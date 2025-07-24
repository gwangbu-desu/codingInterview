import sys
input = sys.stdin.readline

R, C, M = map(int,input().split()) # 격자판 r,c 상어수 M
arr = [[None] * (C+1) for _ in range(R+1)] # R x C

dc = [0,0,1,-1]
dr = [-1,1,0,0]

# shark_list = dict()
answer = 0
for _ in range(M):
    r,c,s,d,z = map(int,input().split()) # 위치 r,c 속력 s 이동 방향 d 크기 z
    arr[r-1][c-1] = (s,d-1,z)
###################### 입력 끝
def change_dir(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2

def shark_move(r, c, s, d):
    if d <= 1:  # 상하 이동
        cycle = 2 * (R - 1)
        s %= cycle
        for _ in range(s):
            if not (0 <= r + dr[d] < R):
                d = change_dir(d)
            r += dr[d]
    else:  # 좌우 이동
        cycle = 2 * (C - 1)
        s %= cycle
        for _ in range(s):
            if not (0 <= c + dc[d] < C):
                d = change_dir(d)
            c += dc[d]
    return r, c, d



def check(nr,nc):
    if 0 <= nr < R and 0 <= nc < C:
        return True
    return False

for i in range(C): # 1th-index, 1. 낚시왕 이동
    # print("상어 이동 전:")
    # for a in range(R):
    #     print(*arr[a], sep=' ')
    #     print()
    # print("상어 이동 후:")
    # 2. 상어 잡기.
    for j in range(R):
        if arr[j][i]:
            s,d,z = arr[j][i] # 상어 잡기
            answer += z
            arr[j][i] = None # 상어 삭제
            break # 제일 위 잡으면 종료
    # 3. 상어 이동.
    temp = [[None] * (C+1) for _ in range(R+1)]
    for r in range(R):
        for c in range(C):
            if arr[r][c]:
                s, d, z = arr[r][c]
                nr, nc, nd = shark_move(r, c, s, d)
                if temp[nr][nc]:
                    # 큰 상어만 살아남음
                    if temp[nr][nc][2] < z:
                        temp[nr][nc] = (s, nd, z)
                else:
                    temp[nr][nc] = (s, nd, z)
    arr = temp  # 다음 턴 상태로 갱신
    # for a in range(R):
    #     print(*arr[a], sep=' ')
    #     print()
    # print()

print(answer)