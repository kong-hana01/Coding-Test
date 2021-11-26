# https://www.acmicpc.net/problem/2191
# 접근방법
# 각 들쥐들의 현재 위치를 기준으로 갈 수 있는 땅굴의 위치를 graph로 저장한다.
# 이를 이분매칭을 사용해 집합을 분리한다.
def dfs(idx):
    if visited[idx]:
        return False
    visited[idx] = True
    for x in graph[idx]:
        if tunnel[x] == -1 or dfs(tunnel[x]):
            tunnel[x] = idx
            return True
    return False


import math
n, m, s, v = map(float, input().split())
graph = [[] for _ in range(int(n))]
tunnel = [-1 for _ in range(int(m))]
mouse = [list(map(float, input().split())) for _ in range(int(n))]
for num in range(int(m)):
    x1, y1 = map(float, input().split())
    for i in range(int(n)):
        x2, y2 = mouse[i]
        if math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) <= s * v:
            graph[i].append(num)

count = 0
for i in range(int(n)):
    visited = [False for _ in range(int(n))]
    if dfs(i):
        count += 1

print(int(n) - count)