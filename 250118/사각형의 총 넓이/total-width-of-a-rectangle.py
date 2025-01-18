n= int(input())

require=[]
max_x = 0
max_y = 0
for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    max_x = max(max_x, x2)
    max_y = max(max_y, y1)
    require.append((x1,y1,x2,y2))

arr = [[0]*max_x for _ in range(max_y)]


for x1,y1,x2,y2 in require:
    for i in range(x1,x2):
        for j in range(y2,y1):
            arr[j][i] = 1

# print(arr)

ans = 0
for i in arr:
    ans += sum(i)

print(ans)