# s(t) = s(t-1) + m + o * (t+2) + s(t-1)

n = int(input())

def s(t):
    if t == 0:
        return 3
    else:
        return s(t-1)*2 + (t+3)
count = 0
while s(count) < n:
    count += 1

def find(N,t):
    if t == 0:
        return "moo"[N-1]
    prev_length = s(t-1)
    middle_length = t+3
    if N<=prev_length:
        return find(N,t-1)
    elif N<=prev_length + middle_length:
        if N == prev_length+1:
            return "m"
        else:
            return "o"
    else:
        return find(N-prev_length - middle_length, t-1)


print(find(n,count))
# a == (a-1) 1 t+2 a-1
# print(dp[count][n-1])