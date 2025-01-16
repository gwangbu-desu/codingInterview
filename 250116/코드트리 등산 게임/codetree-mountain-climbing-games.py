q = int(input())
mountain = []
for _ in range(q):
    arr = list(map(int,input().split()))
    if arr[0] == 100:
        mountain = [0] * arr[1]
        for i in range(arr[1]):
            mountain[i] = arr[i+2]
    elif arr[0] == 200:
        mountain += [arr[1]]
    elif arr[0] == 300:
        mountain = mountain[0:-1]
    elif arr[0] == 400:
        length = len(mountain)
        memoization = [0] * length ## 케이블카 없을때
        cable = [0] * length ## 케이블카 있을때 + 케이블카가 제일 높을 경우

        for i in range(length-1,-1, -1):
            if i==length-1:
                memoization[i] = 0
                continue
            if mountain[i] < mountain[i+1]:
                memoization[i] = memoization[i+1] + 1
            else:
                memoization[i] = memoization[i+1]
        c = max(mountain)
        temp = mountain[0:arr[1]]
        for i in range(arr[1]-1):
            if temp[i] > mountain[arr[1]-1]:
                temp[i] = mountain[arr[1]-1]
        for i in range(arr[1]-1,-1,-1):
            if i==arr[1]-1:
                cable[i] = 1
                continue
            if temp[i] < temp[i + 1]:
                cable[i] = cable[i + 1] + 1
            else:
                cable[i] = cable[i + 1]
        # small = min(memoization)
        # big = max(memoization)
        # if memoization[arr[1]] != small:
        #     print(big*2000000 + max(mountain))
        # else:
        #     print((big+1)*1000000 + max(mountain))
        # 케이블에서 최대 + 케이블카 없을때 최대 + 제일 높은 곳

        # print(temp)
        # print(cable)
        # print(mountain)
        # print(memoization)

        print((max(cable)+max(memoization)) * 1000000 + c)
        #
        # [3, 2, 5, 7, 8, 5, 3, 1, 8, 8]
        # [5, 5, 4,\ 3, 2, 2, 2, 2, 1, 1]
        # [3, 2, 5, 7, 8, 5, 3, 1, 10, 8]
        # [4, 4, 3, 2, 1, 1, 1, 1, 0, 0]
        # 9000010
        #
        # [4, 4, 3, 2, 2, 2, 2, 2, 1, 1]
        # [3, 2, 3, 7, 7, 5, 3, 1, 8, 8]
        # [3, 3, 2, 1, 1, 1, 1, 1, 0, 0]
        # 7000010