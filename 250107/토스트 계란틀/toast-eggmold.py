from collections import deque

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(x, y, nx, ny):
    if 0 <= nx < n and 0 <= ny < n and l <= abs(arr[x][y] - arr[nx][ny]) <= r:
        return True
    return False

def bfs(a, b, visited):
    dq = deque([(a, b)])
    visited[a][b] = True
    positions = [(a, b)]
    total = arr[a][b]
    count = 1

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if check(x, y, nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx, ny))
                positions.append((nx, ny))
                total += arr[nx][ny]
                count += 1

    return total // count, positions

totalCount = 0
while True:
    visited = [[False] * n for _ in range(n)]  # 방문 배열 초기화
    changes = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                avg, positions = bfs(i, j, visited)
                if len(positions) > 1:  # 두 개 이상의 좌표가 연결된 경우만 값 변경
                    changes = True
                    for x, y in positions:
                        arr[x][y] = avg

    if not changes:  # 값 변경이 없으면 종료
        break

    totalCount += 1

print(totalCount)
