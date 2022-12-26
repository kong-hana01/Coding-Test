# https://www.acmicpc.net/problem/2610
# 접근 방법
# 분리집합을 사용해 집합을 나눈 뒤 BFS를 통해 총 점수를 각각 구하여 각 집합별 제일 낮은 점수의 번호를 출력한다.
def get_parent(node):
    if parent[node] == node:
        return node
    parent[node] = get_parent(parent[node])
    return parent[node]

def find_union(node1, node2):
    parent1, parent2 = get_parent(node1), get_parent(node2)
    parent[parent2] = parent1

def bfs(node):
    visited[node] = 0
    queue = deque([])
    queue.append(node)
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visited[next] == -1:
                queue.append(next)
                visited[next] = visited[now] + 1

import sys
from collections import deque
input = sys.stdin.readline
n, m = int(input()), int(input())
graph = [[] for _ in range(n+1)] # 양방향 그래프
parent = [i for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    find_union(a, b)

children = {}
for i in range(1, n+1):
    p = get_parent(i)
    if p not in children.keys():
        children[p] = []
    children[p].append(i)

result = []
for lst in children.values():
    minScore = 10000
    for x in lst:
        visited = [-1 for _ in range(n+1)]
        bfs(x)
        score = max(visited)
        if minScore > score:
            minScore = score
            minNum = x
    result.append(minNum)
result.sort()
print(len(children), *result, sep='\n')