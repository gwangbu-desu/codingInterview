dx=[1,0,-1,0]
dy=[0,-1,0,1]
curve_list=[]

n = int(input())

arr=[[False] * (102) for _ in range(102)] # 빈 배열 만들기
cmds= []
max_g = 0
answer = 0
for i in range(n):
    x,y,d,g = map(int,input().split())
    cmds.append((x,y,d,g))
    max_g = max(max_g,g)

######################함수
def make_curve(g): # 방향은 0기준으로, g는 최대값 기준으로
    global curve_list
    count = 0
    curve = [0]
    curve_list.append(curve)
    while count != g:
        before = curve_list[count][:]
        count += 1
        length = len(before)
        for i in range(length):
            before.append((before[length - 1 - i]+1)%4)
        curve_list.append(before) # 현재 세대 드래곤 커브 저장

    # print(*curve_list)

def mark(x,y,d,g):
    global arr
    nx, ny = x,y
    arr[y][x] = True
    curve = curve_list[g]
    for i in curve:
        nx = nx + dx[(i + d)%4]
        ny = ny + dy[(i + d)%4]
        arr[ny][nx] = True

def find_rect(x,y):
    global arr
    if arr[y][x] and arr[y+1][x] and arr[y+1][x+1] and arr[y][x+1]:
        return True
    return False
#####################함수
make_curve(max_g)
for cmd in cmds:
    mark(*cmd)

################### 사각형 찾기
for i in range(101):
    for j in range(101):
        if find_rect(i,j):
            answer += 1

print(answer)