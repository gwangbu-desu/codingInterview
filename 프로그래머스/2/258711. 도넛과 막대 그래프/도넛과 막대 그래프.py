def solution(edges):
    answer = [0]*4
    length = max(map(max,edges))
    in_put = [0]*(length+1)
    output = [0]*(length+1)
    for a,b in edges:
        in_put[b]+=1
        output[a]+=1
    # print(in_put,output)
    for i in range(1,length+1):
        if in_put[i] ==0 and output[i]>=2:
            answer[0]=i
        elif in_put[i]>0 and output[i]==0:
            answer[2]+=1
        elif in_put[i]>=2 and output[i]>=2:
            answer[3]+=1
    answer[1]=output[answer[0]] - answer[2] - answer[3]
    return answer