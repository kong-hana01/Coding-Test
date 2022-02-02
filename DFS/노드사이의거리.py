# https://www.acmicpc.net/problem/1240
# 접근 방법
# 리스트를 통해 트리를 구현한 뒤 DFS를 통해 거리를 측정한다.
# 트리로 구현됬기에 각 노드간의 거리는 DFS를 통해 이동했을 때가 가장 최소한의 거리이기에 찾고자하는 위치가 나온 경우 바로 리턴한 뒤, 값을 출력한다.
def dfs(node1, node2, dist):
    visited[node1] = True
    if node1 == node2:
        return dist
    for x, d in nodes[node1]:
        if visited[x]:
            continue
        result = dfs(x, node2, dist+d)
        if result:
            return result
    return 0
    

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
nodes = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v, cost = map(int, input().split())
    nodes[u].append([v, cost])
    nodes[v].append([u, cost])
for _ in range(m):
    u, v = map(int, input().split())
    visited = [False for _ in range(n+1)]
    print(dfs(u, v, 0))