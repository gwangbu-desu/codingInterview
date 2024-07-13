from collections import deque

n, l = map(int,input().split(" "))

maze = [list(map(int,input().split(" "))) for _ in range(n)]

# def up():

# def down():

def check_column(idx:int) -> bool:
    result = []
    lst = []
    for i in range(n):
        lst.append(maze[idx][i])
    buffer = []
    for i in lst:
        if buffer:
            if buffer[0] != i:
                result.append([buffer[0],len(buffer)])
                buffer = [i]
            else:
                buffer.append(i)
        else:
            buffer.append(i)
    result.append([buffer[0],len(buffer)])
    return check_lst(result)


def check_lst(lst:list) -> bool:
    length = len(lst)
    if length == 1:
        return True
    for i in range(len(lst)-1):
        if abs(lst[i][0] - lst[i+1][0]) != 1:
            return False
        if lst[i][0] < lst[i+1][0] and lst[i][1] < l: # 경사로 길이가 충분하지 않을 경우(현재위치가 아래)
            return False
        elif lst[i][0] > lst[i+1][0] and lst[i+1][1] < l: # 경사로 길이가 충분하지 않을 경우(현재위치가 위)
            return False
        elif lst[i][0] > lst[i+1][0] and lst[i+1][1] >= l:
            lst[i+1][1] -= l
    return True 

def check_row(idx:int) -> bool:
    result = []
    lst = []
    for i in range(n):
        lst.append(maze[i][idx])
    buffer = []
    for i in lst:
        if buffer:
            if buffer[0] != i:
                result.append([buffer[0],len(buffer)])
                buffer = [i]
            else:
                buffer.append(i)
        else:
            buffer.append(i)
    result.append([buffer[0],len(buffer)])
    return check_lst(result)

sum = 0
for i in range(n):
    if check_column(i):
        sum += 1
    if check_row(i):
        sum += 1

print(sum)
# (숫자, 연속된 길이)