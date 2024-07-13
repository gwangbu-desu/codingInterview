# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1,11):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    arr = list(map(int,input().split(" ")))
    result = 0
    for i in range(2,len(arr)-2):
        #print(i)
        m1 = max(arr[i-2:i])
        m2 = max(arr[i+1:i+3])
        m3 = max(m1,m2)
        #print(m3)
        #print(m3,arr[i])
        if arr[i] > m3:
            result+=(arr[i]-m3)
    print("#",end="")
    print(test_case,end=" ")
    print(result)
    
    # ///////////////////////////////////////////////////////////////////////////////////
