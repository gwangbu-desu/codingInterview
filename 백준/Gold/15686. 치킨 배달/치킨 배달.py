import sys
input = sys.stdin.readline
n,m = map(int,input().split()) # 도시 크기, 유지할 치킨집 수
arr=[]

house = []
chicken = []
answer = float('inf')
for i in range(n):
    tmp = list(map(int,input().split()))
    arr.append(tmp)
    for j in range(n):
        if tmp[j] == 1:
            house.append((i,j)) # 행,열
        elif tmp[j] == 2:
            chicken.append((i,j)) # 행,열
################################ 입력
# 치킨집 거리 계산
def distance(c_list):
    dist = 0
    for i,j in house:
        min_dist = float('inf')
        for k,l in c_list:
            min_dist = min(min_dist,abs(k - i) + abs(l - j))
        dist += min_dist
    return dist

# 백트래킹 사용해서 m개를 종료 조건으로 설정.
def dfs(c_list,idx):
    global answer
    # if m > len(c_list) > 0:
    #     # 치킨집 거리 계산
    #     dist = distance(c_list)
    #     # 최소값 업데이트
    #     answer = min(dist, answer)
    if len(c_list) == m or idx == len(chicken):
        # 치킨집 거리 계산
        dist = distance(c_list)
        # 최소값 업데이트
        answer = min(dist, answer)
        return

    x,y = chicken[idx]
    if (x,y) not in c_list:
        dfs(c_list + [(x,y)],idx+1)
        dfs(c_list,idx+1)

dfs([],0)

print(answer)