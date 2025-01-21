
n = int(input())
employee = list(map(int, input().split()))
company = list(map(int, input().split()))

# DP 테이블 초기화
# dp[i][used]는 i번째 직원까지 배치했을 때, 사용된 회사 상태가 used일 경우 가능한 경우의 수
dp = [[0] * (1 << n) for _ in range(n + 1)]
dp[0][0] = 1  # 초기 상태

# 회사 사용 상태를 리스트로 대체
used_states = [[False] * n for _ in range(1 << n)]

for i in range(n):  # i번째 직원
    for mask in range(1 << n):  # 모든 사용 상태 탐색
        if dp[i][mask] == 0:  # 유효하지 않은 상태는 건너뜀
            continue

        for j in range(n):  # j번째 회사
            if not (mask & (1 << j)) and company[j] >= employee[i]:
                dp[i + 1][mask | (1 << j)] += dp[i][mask]  

print(dp[n][(1 << n) - 1])