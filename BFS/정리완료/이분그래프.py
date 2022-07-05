# https://www.acmicpc.net/problem/1707
# 접근 방법
# BFS를 통해 한 정점을 1, 다른 정점을 2으로 바꿔가며 이를 갱신하다가 모든 정점을 문제없이 분할할 수 있다면 YES, 아니면 NO를 출력한다.
from collections import deque
import sys
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        u1, u2 = map(int, input().split())
        graph[u1].append(u2)
        graph[u2].append(u1)
    visited = [0 for _ in range(v+1)]
    is_bipartite_graph = True
    visited_of_nodes = v
    while visited_of_nodes > 0 and is_bipartite_graph:
        
        for i in range(1, v+1):
            if not visited[i]:
                queue = deque([])
                queue.append([i, 1]) # 정점, 번호
                visited[i] = 1
                visited_of_nodes -= 1
                break
            
        while queue and is_bipartite_graph:
            node, num = queue.popleft()
            num = (num % 2 + 1)
            for u in graph[node]:
                if not visited[u]:
                    visited[u] = num
                    queue.append([u, num])
                    visited_of_nodes -= 1
                elif visited[u] != num:
                    is_bipartite_graph = False
                    break

    if is_bipartite_graph:
        print('YES')
    else:
        print('NO')

# https://www.acmicpc.net/problem/1707
# 접근 방법 -> 실패
# 0. 주어진 그래프를 저장하며 각 정점에 대한 리스트를 만들고, 그 리스트의 값은 0으로 저장한다.
# 1. DFS를 통해 각 정점을 탐색하되, (이전 정점의 값) % 2 + 1을 해서 정점의 집합을 구분해준다.
# 2. 만약 현재 탐색 중인 그래프의 정점이 0이면 1번대로 값을 갱신해준다.
# 3. 만약 현재 탐색 중인 그래프의 정점이 0이 아니고, 1번대로 값을 갱신해줄 때의 값과 동일하다면 TRUE를 리턴해준다.
# 4. 만약 현재 탐색 중인 그래프의 정점이 0이 아니고, 1번대로 값을 갱신해줄 때의 값과 다르다면 False를 리턴해주고, DFS를 종료한다.
def dfs(v, union):
    if not vertex[v]: vertex[v] = union
    elif vertex[v] != union: return 0
    elif visited[v]: return vertex[v]
    
    visited[v] = True
    for x in graph[v]:
        if not visited[x]:
            next_union = union%2 + 1 if union else 0
            next = dfs(x, next_union)
            if not next:
                return 0   
            vertex[v] = next%2 + 1

    return union

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
tc = int(input())
for _ in range(tc):
    v, e = map(int, input().split())
    vertex = [0 for _ in range(v+1)]
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    is_false = False
    vertex[1] = 1
    for i in range(1, v+1):
        visited = [False for _ in range(v+1)]
        if not dfs(i, vertex[i]):
            is_false = True
            break

    if is_false: print('NO')
    else: print("YES")