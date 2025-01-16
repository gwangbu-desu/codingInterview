n = int(input())

peopleList = []
for _ in range(n):
    arrive_t, test_t = map(int,input().split())
    peopleList.append((arrive_t,test_t))
peopleList.sort()
total = 0
end_time = 0
for a,t in peopleList:
    if end_time > a:
        end_time += t
    else:
        end_time = a + t
print(end_time)