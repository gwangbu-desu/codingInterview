n = int(input())

employee = list(map(int,input().split()))

company = list(map(int,input().split()))

ans = 0
def bt(remains:list,idx:int):
    global ans
    if idx == n-1 and remains[0] >= employee[idx]:
        ans += 1
    for index,value in enumerate(remains):
        if value >= employee[idx]:
            bt(remains[:index] + remains[index+1:], idx+1)

bt(company,0)
print(ans)