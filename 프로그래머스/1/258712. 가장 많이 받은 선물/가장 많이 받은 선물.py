from itertools import combinations

def compare(s,r,arr,si,ri):
    if s>r:
        arr[si]+=1
        return False
    elif r>s:
        arr[ri]+=1
        return False
    else:
        return True

def solution(friends, gifts):
    n=len(friends)
    str2idx={name:i for i ,name in enumerate(friends)}
    next_gift = [0]*n
    gift_mat = [[0]*n for _ in range(n)]
    gift_indices = [0 for _ in range(n)]
    
    for val in gifts:
        sender, receiver = val.split()
        si, ri = str2idx[sender] ,str2idx[receiver]
        gift_mat[si][ri] += 1
        gift_indices[si] += 1
        gift_indices[ri] -=1
    for si, ri in combinations(range(n),2):
        sr = gift_mat[si][ri]
        rs = gift_mat[ri][si]
        if compare(sr,rs,next_gift,si,ri):
            s=gift_indices[si]
            r=gift_indices[ri]
            compare(s,r,next_gift,si,ri)
            pass
        pass
    return max(next_gift)