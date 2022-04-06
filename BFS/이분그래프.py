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