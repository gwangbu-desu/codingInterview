n=int(input())
arr=[] #입력 받은 배열
for i in range(n):
    arr.append(list(input()))

weight=dict() #몇번째 자리에서 알파벳이 등장했는지
for i in arr:
    for j in range(len(i)):
        try:
            weight[i[j]]+=10**(len(i)-j)
        except Exception:
            weight[i[j]]=10**(len(i)-j)

weights = sorted(weight.items(),key=lambda x:x[1], reverse=True)
count=9

value=dict()
for i in weights:
    value[i[0]]=count
    count-=1
result =0
for i in arr:
    for j in range(len(i)):
        result += (10**(len(i)-j-1))*value[i[j]]

print(result)