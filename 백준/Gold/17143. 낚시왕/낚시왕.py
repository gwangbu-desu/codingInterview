import sys
input = sys.stdin.readline

R, C, M = map(int,input().split()) # 격자판 r,c 상어수 M
arr = [[False] * (C+1) for _ in range(R+1)] # R x C

dc = [0,0,1,-1]
dr = [-1,1,0,0]

shark_list = dict()
answer = 0
for _ in range(M):
    r,c,s,d,z = map(int,input().split()) # 위치 r,c 속력 s 이동 방향 d 크기 z
    shark_list[(r-1,c-1)] = (s,d-1,z)
    arr[r-1][c-1] = True
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

def shark_move(r,c,s,d):
    nr = r
    nc = c
    nd = d
    for i in range(s):
        rr = nr + dr[nd]
        cc = nc + dc[nd]
        if check(rr,cc): # 갈 수 있음
            nr = rr
            nc = cc
        else: # 갈 수 없음 -> 방향 전환해서 전진
            nd = change_dir(nd)
            nr += dr[nd]
            nc += dc[nd]

    return nr, nc, nd


def check(nr,nc):
    if 0 <= nr < R and 0 <= nc < C:
        return True
    return False

for i in range(0,C): # 1th-index, 1. 낚시왕 이동
    # print("상어 이동 전:")
    # for a in range(R):
    #     print(*arr[a], sep=' ')
    #     print()
    # print("상어 이동 후:")
    # 2. 상어 잡기.
    for j in range(R):
        if arr[j][i]:
            s,d,z = shark_list.pop((j,i)) # 상어 잡기
            answer += z
            arr[j][i] = False # 상어 삭제
            break # 제일 위 잡으면 종료
    # 3. 상어 이동.
    new_shark_list = dict()
    for key, value in shark_list.items():
        r,c = key
        s,d,z = value
        nr, nc, nd = shark_move(r,c,s,d) # 이동 완료
        if new_shark_list.get((nr,nc),None): # 있다면 크기 비교
            _,_,origin = new_shark_list.get((nr,nc))
            if origin < z:
                new_shark_list[(nr,nc)] = (s,nd,z)
        else: # 해당 칸에 상어가 없으면 저장
            new_shark_list[(nr,nc)] = (s,nd,z)
        arr[r][c] = False # 기존 상어 위치는 없애기
    shark_list = new_shark_list # 새 상어 위치로 덮어버림
    for key, value in shark_list.items():
        r,c = key
        arr[r][c] = True # 새 상어 위치
    # for a in range(R):
    #     print(*arr[a], sep=' ')
    #     print()
    # print()

print(answer)