def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    dictionary = {"code":0,"date":1,"maximum":2,"remain":3}
    ext_idx=dictionary[ext]
    ext_sort=dictionary[sort_by]
    result=[]
    for i in data:
        if(i[ext_idx]<val_ext):
            result.append(i)
    answer = sorted(result,key=lambda x:x[ext_sort])
    return answer

