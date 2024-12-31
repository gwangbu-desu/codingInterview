from collections import deque

# import sys
# sys.stdin = open("input.txt", "r")
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    arr = [list(map(int, input().split(" "))) for _ in range(4)]
    # print(arr)
    result = set()


    def dfs(x, y, num, depth: int):
        if depth == 6:
            result.add(num)
            # print(num)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                dfs(nx, ny, num + str(arr[nx][ny]), depth + 1)


    visited = []
    for i in range(4):
        for j in range(4):
            if arr[i][j] in visited:
                continue
            dfs(i,j,str(arr[i][j]), 0)

    print(f"#{test_case} {len(result)}")

    # ///////////////////////////////////////////////////////////////////////////////////
