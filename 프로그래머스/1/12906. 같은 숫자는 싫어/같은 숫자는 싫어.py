def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    result = [False]*10
    for i in arr:
        if result[i]==False:
            result = [False]*10
            answer.append(i)
            result[i]=True
    return answer