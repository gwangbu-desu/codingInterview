from collections import deque

def solution(queue1, queue2):
    answer = 0
    length = len(queue1)+len(queue2)
    arr1 = deque(queue1)
    arr2 = deque(queue2)
    sum1=sum(arr1)
    sum2=sum(arr2)
    if((sum1+sum2)%2==1):
        return -1
    while(sum1!=sum2):
        if(sum1>sum2):
            temp = arr1.popleft()
            # print(temp)
            arr2.append(temp)
            sum1-=temp
            sum2+=temp
        else:
            temp = arr2.popleft()
            arr1.append(temp)
            sum1+=temp
            sum2-=temp
        answer+=1
        if(answer>length*4):
            return -1
    return answer