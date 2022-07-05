# https://www.acmicpc.net/problem/25195
# 접근 방법
# DFS를 통해 곰곰이를 만나는지 만나지 못하는지 체크하여 출력한다.
# 해당 문제에는 사이클이 없기에 곰곰이의 위치에는 방문처리를 해 문제를 해결한다.
def dfs(s):
    visited[s] = True
    is_meet = not bool(graph[s])
    for u in graph[s]:
        if not visited[u] and dfs(u):
            return True
    return is_meet

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
visited = [False for _ in range(n+1)]
s = int(input())
for x in list(map(int, input().split())):
    visited[x] = True
print("Yes" if visited[1] or not dfs(1) else "yes")
