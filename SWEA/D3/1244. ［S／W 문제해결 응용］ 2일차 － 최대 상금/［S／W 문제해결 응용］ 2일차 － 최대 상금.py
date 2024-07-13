T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 값 높은거, 인덱스 낮은 거 기준으로 swap을 진행 rotate횟수만큼.
def bt(lst:list, depth:int):
    global mmax
    global visited
    global rotate
    if depth == rotate:
        mmax = max(int("".join(lst)),mmax)
        return
    lngth = len(lst)
    for i in range(lngth-1):
        for j in range(i+1,lngth):
            lst[i],lst[j]=lst[j], lst[i]
            if (".".join(lst),depth) not in visited:
                bt(lst,depth+1)
                visited.add((".".join(lst),depth))
            lst[i],lst[j]=lst[j], lst[i]
            
            
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, rotate = map(int,input().split(" "))
    s = []
    arr = list(str(n))
    visited = set()
    mmax = 0
    bt(arr,0)
    print("#",end="")
    print(test_case,end=" ")
    print(mmax)
    #for i in range(rotate):
        
    # ///////////////////////////////////////////////////////////////////////////////////
