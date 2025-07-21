from collections import deque

n = int(input())
# arr = [[0]*n for i in range(n)] # 전체 지도 n x n
apple = set()
k = int(input()) # 사과 개수
for i in range(k): # 사과 위치
    row, col = map(int,input().split())
    apple.add((row,col))

l = int(input())

directions = dict()
for i in range(l):
    x,c = map(str,input().split())
    directions[int(x)] = c


timer = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]
# L이면 1%4, D이면 -1%4

# 첫 시작은 오른쪽 = 0
direct = 0
current_row = 1
current_col = 1
snake_body=deque([(current_row,current_col)])
while True:
    # 1초 증가
    timer += 1
    current_row,current_col = snake_body.popleft() # 머리
    snake_body.appendleft((current_row,current_col))
    # 뱀 이동 - deque에 머리 추가
    nr = current_row + dy[direct]
    nc = current_col + dx[direct]
    # 머리가 벽과 부딪히는지 확인
    if nr < 1 or nr > n or nc < 1 or nc > n:
        break
    if (nr,nc) in snake_body:
        break
    snake_body.appendleft((nr, nc))
    # 뱀 pop 여부 확인 (사과 확인)
    if (nr,nc) not in apple:
        snake_body.pop() # 꼬리 빼기
    else:
        apple.remove((nr,nc)) # 먹은  사과 제거

    if directions.get(timer,None) is not None:
        if directions[timer] == "D":
            direct = (direct + 1)%4
        elif directions[timer] == "L":
            direct = (direct - 1)%4

print(timer)

