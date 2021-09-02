# 접근 방법
# 주어진 정점에 대해 그래프로 입력을 받은 뒤, 부모 노드부터 dfs탐색을 진행해 탐색하지 않은 노드를 인덱스로 하는 리스트의 값에 이미 탐색한 노드를 저장하고 탐색하지 않은 노드를 dfs탐색한다.
def dfs(node):  
    for x in graph[node]:
        if not parent[x]:
            parent[x] = node
            dfs(x)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]
parent[1] = 1
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
for i in range(2, n+1):
    print(parent[i])