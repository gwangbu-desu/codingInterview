n,k =map(int,input().split(" "))
arr = []
for i in range(n):
    arr.append(int(input()))
dp=[0]*(k+1)
dp[0]=1 #아무동전도 사용되지 않는 경우
for i in arr: #모든 동전이 사용되는 경우 순회
    for j in range(i,k+1): #가치의 경우 순회
        dp[j]+=dp[j-i] # j원을 만족하기 위해 j-i원의 경우를 더해줌 j-1원의 가지수 + i원을 하면 j-i만큼의 가지수가 추가됨

print(dp[k])