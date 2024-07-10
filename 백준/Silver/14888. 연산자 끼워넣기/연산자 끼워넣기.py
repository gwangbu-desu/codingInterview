from itertools import permutations
mmax = -1000000000
mmin = 1000000000
n= int(input())
lst = list(map(int,input().split(" ")))

op = list(map(int, input().split(" "))) # + - x /

op_list=[]
def cal(x,y,op):
    if op==0:
        return x+y
    elif op==1:
        return x-y
    elif op==2:
        return x*y
    elif op==3:
        return divide(x,y)

def divide(x,y):
    result =0
    if(x<0):
        result = x*(-1) // y
        return result*(-1)
    else:
        return x//y

for i in range(4):
    op_list+=[i]*op[i]


for i in permutations(op_list,n-1):
    start = lst[0]
    operations = list(i)
    for j in range(n-1):
        start = cal(start,lst[j+1],operations[j])
    mmax = max(mmax,start)
    mmin = min(mmin,start)

print(mmax)
print(mmin)