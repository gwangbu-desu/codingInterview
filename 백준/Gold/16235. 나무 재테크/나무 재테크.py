import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
dr = [-1,-1,-1,0,0,1,1,1]
dc = [-1,0,1,-1,1,-1,0,1]
class Land:
    global arr
    def __init__(self,energy):
        self.energy = energy
        self.tree_list = []
        self.dead_tree_list = []

    def tree_add(self, age):
        # heapq.heappush(self.tree_list,age)
        self.tree_list.append(age)

    def spring(self):
        alive = []
        dead = []
        self.tree_list.sort()
        for i in range(len(self.tree_list)):
            age = self.tree_list[i]
            if self.energy >= age:
                self.energy -= age
                alive.append(age + 1)
            else:
                dead = self.tree_list[i:]
                break
        self.tree_list = alive
        self.dead_tree_list = dead
    def summer(self):
        for i in self.dead_tree_list:
            self.energy += i//2
        self.dead_tree_list.clear() # 비우기

    def fall(self,r,c):
        for i in self.tree_list:
            if i % 5 == 0: # 5배수 일때,
                for j in range(8):
                    nr = r + dr[j]
                    nc = c + dc[j]
                    if check(nr,nc):
                        arr[nc][nr].tree_add(1) # 나무 추가

    def add_energy(self,energy):
        self.energy += energy

    def count_tree(self):
        return len(self.tree_list)
def cmd(cmd):
    if cmd == 1:
        for i in range(N):
            for j in range(N):
                arr[j][i].spring()
    elif cmd == 2:
        for i in range(N):
            for j in range(N):
                arr[j][i].summer()
    elif cmd == 3:
        for i in range(N):
            for j in range(N):
                arr[j][i].fall(i,j)
    elif cmd == 4:
        for i in range(N):
            for j in range(N):
                arr[j][i].add_energy(give_energy[i][j])

def check(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

arr = [[Land(5) for _ in range(N)]  for _ in range(N)] # 1부터 N까지, 1-index-> 0-index | 양분, 나무

give_energy = []
for i in range(N):
    tmp = list(map(int,input().split()))
    give_energy.append(tmp)

for i in range(M):
    x,y,z = map(int,input().split()) # 심은 나무 정보
    arr[y-1][x-1].tree_add(z) # 0-index로 만들기

# # 초기 땅
# for r in range(N):
#     for c in range(N):
#         print(arr[c][r].count_tree(),end=' ')
#     print()
# print("에너지")
#
# # 초기 에너지
# for r in range(N):
#     for c in range(N):
#         print(arr[c][r].energy,end=' ')
#     print()
# print("나무")
#
# # 초기 나무
# for r in range(N):
#     for c in range(N):
#         print(*arr[c][r].tree_list,end=' ')
#     print()
# print("")
for i in range(K): # K 년후 남아 있는 나무 개수 구하기.
    # print(f"#{i}년")
    # for r in range(N):
    #     for c in range(N):
    #         print(arr[c][r].count_tree(),end=' ')
    #     print()
    # print("에너지")
    # for r in range(N):
    #     for c in range(N):
    #         print(arr[c][r].energy,end=' ')
    #     print()
    # print("나무")
    #
    # # 초기 나무
    # for r in range(N):
    #     for c in range(N):
    #         print(*arr[c][r].tree_list, end=' ')
    #     print()
    # print()
    # 봄, 여름, 가을, 겨울 반복
    for j in range(1,5):
        cmd(j)


answer = 0
for i in range(N):
    for j in range(N):
        answer += arr[j][i].count_tree()

print(answer)