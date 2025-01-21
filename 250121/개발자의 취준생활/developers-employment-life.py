n = int(input())
employee = list(map(int, input().split()))
company = list(map(int, input().split()))

ans = 0

def bt(used: list, idx: int):
    global ans
    if idx == n:  # 모든 직원의 요구를 충족한 경우
        ans += 1
        return

    for i, c in enumerate(company):
        if not used[i] and c >= employee[idx]:
            used[i] = True  # 회사 자원을 사용
            bt(used, idx + 1)
            used[i] = False  # 되돌리기

# 회사 자원 사용 여부를 추적하기 위한 배열
used = [False] * n
bt(used, 0)

print(ans)
