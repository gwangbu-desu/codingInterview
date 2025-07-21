n,m,y,x,k = map(int,input().split())

arr = [[0] * m for _ in range(n)] # 지도
for i in range(n):
    tmp = list(map(int,input().split()))
    arr[i] = tmp

dice=[0,0,0,0,0,0]

def command(direct):
    global dice
    if direct==1: # 동쪽
        dice = [dice[3]] + [dice[1]] + [dice[0]] + [dice[5]] + [dice[4]] + [dice[2]]
    elif direct==2: # 서쪽
        dice = [dice[2]] + [dice[1]] + [dice[5]] + [dice[0]] + [dice[4]] + [dice[3]]
    elif direct==3: # 북쪽
        dice = [dice[4]] + [dice[0]] + [dice[2]] + [dice[3]] + [dice[5]] + [dice[1]]
    elif direct==4: # 남쪽
        dice = [dice[1]] + [dice[5]] + [dice[2]] + [dice[3]] + [dice[0]] + [dice[4]]

cmds = map(int,input().split())
for cmd in cmds:
    if cmd == 1: # 동쪽
        nx = x + 1
        if nx >= m or nx < 0:
            continue
        else:
            x = nx
    elif cmd == 2:
        nx = x - 1
        if nx >= m or nx < 0:
            continue
        else:
            x = nx
    elif cmd == 3:
        ny = y - 1
        if ny >= n or ny < 0:
            continue
        else:
            y = ny
    elif cmd == 4:
        ny = y + 1
        if ny >= n or ny < 0:
            continue
        else:
            y = ny

    command(cmd)
    if arr[y][x] == 0:
        # 0 이면,
        arr[y][x] = dice[5]
    else: # 0이 아니면
        dice[5] = arr[y][x] # 주사위 바닥면의 값을 복사
        arr[y][x] = 0 # 지도는 0 채우기

    print(dice[0]) # 윗면 출력


