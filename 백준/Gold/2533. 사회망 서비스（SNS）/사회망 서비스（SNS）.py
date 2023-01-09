# https://www.acmicpc.net/problem/2533
# 접근 방법
# DFS를 통해 문제를 해결한다.
def dfs(now):
    visited[now] = True
    if not graph[now]:
        dp[now][1] = 1
        
    for next in graph[now]:
        if visited[next]:
            continue
        temp = dfs(next)
        dp[now][0] += temp[1]
        dp[now][1] += min(temp)
    dp[now][1] += 1
    return dp[now]


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
dp = [[0, 0] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
dfs(1)
print(min(dp[1]))