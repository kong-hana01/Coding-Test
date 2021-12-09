# https://www.acmicpc.net/problem/18138
# 접근 방법
# 주어진 조건(w/2<=세일러카라<=w*3/4 or w<=세일러카라<=w*5/4)에 따라 이분매칭을 진행하여 만들 수 있는 세일러복의 최댓값을 출력한다.
def dfs(idx):
    if visited[idx]:
        return False
    visited[idx] = True
    for x in t[idx]:
        if c[x] == -1 or dfs(c[x]):
            c[x] = idx
            return True
    return False

n, m = map(int, input().split())
width_t = [int(input()) for _ in range(n)]
width_c = [int(input()) for _ in range(m)]
t = [[] for _ in range(n)]
c = [-1 for _ in range(m)]
for i in range(n):
    w = width_t[i]
    for j in range(m):
        if w/2<=width_c[j]<=w*3/4 or w<=width_c[j]<=w*5/4:
            t[i].append(j)

count = 0
for i in range(n):
    visited = [False for _ in range(n)]
    if dfs(i):
        count += 1
print(count)