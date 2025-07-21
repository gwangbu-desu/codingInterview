from copy import deepcopy


def watch(type):
    if type == 1:
        return 0b0001, 4
    elif type == 2:
        return 0b0101, 2
    elif type == 3:
        return 0b0011, 4
    elif type == 4:
        return 0b0111, 4
    elif type == 5:
        return 0b1111, 1


def rotate_left(val):
    return ((val << 1) | (val >> 3)) & 0b1111  # 4비트 왼쪽 회전


# 방향: 동, 서, 북, 남 (bit와 index 일치)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 입력
y, x = map(int, input().split())
arr = []
cctv_list = []
for i in range(y):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    for idx, value in enumerate(tmp):
        if 1 <= value <= 5:
            cctv_list.append((i, idx, value))  # y, x, CCTV 번호


# 감시 마킹
def mark(board, y, x, bit):
    for d in range(4):
        if (bit & (1 << (3 - d))):
            ny, nx = y, x
            while True:
                ny += dy[d]
                nx += dx[d]
                if not (0 <= ny < len(board) and 0 <= nx < len(board[0])):
                    break
                if board[ny][nx] == 6:
                    break
                if board[ny][nx] == 0:
                    board[ny][nx] = '#'
                # 감시 중복 가능하므로 CCTV도 통과, '#'도 통과


min_blind = float('inf')


# DFS로 모든 회전 조합 탐색
def dfs(depth, board):
    global min_blind
    if depth == len(cctv_list):
        blind = sum(row.count(0) for row in board)
        min_blind = min(min_blind, blind)
        return

    y_, x_, type_ = cctv_list[depth]
    bit, rot_count = watch(type_)

    for _ in range(rot_count):
        new_board = deepcopy(board)
        mark(new_board, y_, x_, bit)
        dfs(depth + 1, new_board)
        bit = rotate_left(bit)


dfs(0, arr)
print(min_blind)
