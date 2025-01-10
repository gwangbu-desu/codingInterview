n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

exit_condition = n//2

minimum = 100000

def cal(lst):
    result = 0
    for i in range(exit_condition):
        for j in range(i):
            result += arr[lst[i]][lst[j]] + arr[lst[j]][lst[i]]
    return result

def back(alst, blst, idx):
    global minimum
    if len(alst) == len(blst) and idx == n:
        minimum = min(minimum, abs(cal(alst) - cal(blst)))
        return
    if len(alst) > exit_condition or len(blst)>exit_condition:
        return

    back(alst+[idx], blst, idx+1)
    back(alst,blst + [idx], idx+1)

back([],[],0)
print(minimum)