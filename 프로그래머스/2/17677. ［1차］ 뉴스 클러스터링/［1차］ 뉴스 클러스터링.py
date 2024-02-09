from collections import Counter

def encoding(str):
    new = str.lower()
    result=[]
    for i in range(len(new)-1):
        if(new[i].isalpha() and new[i+1].isalpha()):
            result.append(new[i]+new[i+1])
    return result
        
def solution(str1, str2):
    answer = 0
    first=Counter(encoding(str1))
    second=Counter(encoding(str2))
    union=list((first|second).elements())
    intersact=list((first&second).elements())
    if len(union) ==0 and len(intersact)==0:
        return 65536
    return int(len(intersact)/len(union)*65536)