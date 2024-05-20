def solution(wallpaper):
    answer = []
    left=51
    right=0
    top=0
    bottom=51
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if(wallpaper[i][j]=='#'):
                left=min(left,i)
                right=max(right,i)
                top=max(top,j)
                bottom=min(bottom,j)
    answer.append(left)
    answer.append(bottom)
    answer.append(right+1)
    answer.append(top+1)
    return answer