n = int(input())
custom_n = list(map(int,input().split()))

boss, member = map(int,input().split())

total = 0

for i in custom_n:
    i -= boss
    total += 1 + i // member
    i = i%member
    if i > 0:
        total += 1

print(total)