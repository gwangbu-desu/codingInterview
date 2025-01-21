n = int(input())
employee = list(map(int, input().split()))
company = list(map(int, input().split()))

# DP 테이블 초기화
dp = [[0] * (1 << n) for _ in range(n + 1)]
dp[0][0] = 1  # 초기 상태

# DP 상태 전이
for i in range(n):  # i번째 직원
    for mask in range(1 << n):  # 현재 회사 자원의 사용 상태
        if dp[i][mask] == 0:
            continue  # 유효하지 않은 상태는 건너뜀
        for j in range(n):  # j번째 회사
            if not (mask & (1 << j)) and company[j] >= employee[i]:
                dp[i + 1][mask | (1 << j)] += dp[i][mask]

# 최종 결과
print(dp[n][(1 << n) - 1])
