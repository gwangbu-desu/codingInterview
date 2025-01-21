from itertools import permutations

# 입력
n = int(input())
employee = list(map(int, input().split()))
company = list(map(int, input().split()))

# 가능한 회사 순열 생성
company_indices = list(range(n))
permutations_of_companies = permutations(company_indices)

# 가능한 배치 수 계산
result = 0
for perm in permutations_of_companies:
    valid = True
    for i in range(n):
        if company[perm[i]] < employee[i]:
            valid = False
            break
    if valid:
        result += 1

# 출력
print(result)
