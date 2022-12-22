# https://www.acmicpc.net/problem/16964
# 접근 방법
# 그래프 엣지를 표현할 때 set으로 데이터를 저장해 문제를 해결한다.
def dfs(now):
    global now_index
    now_index += 1
    visited[now] = True

    if now_index == n:
        return True
    while visited_seq[now_index] in graph[now]:
        if dfs(visited_seq[now_index]):
            return True


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
graph = [set([]) for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
visited_seq = list(map(int, input().split()))
if visited_seq[0] != 1:
    print(0)
else:
    now_index = 0
    dfs(1)
    print(0 if False in visited[1:] else 1)