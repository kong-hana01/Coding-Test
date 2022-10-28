# https://www.acmicpc.net/problem/16932
# 접근 방법
# BFS로 집합을 만든 뒤, 0의 위치를 따로 저장하고, 그 0을 1로 바꿨을 때의 상하좌우의 집합을 연결해 최대 개수를 구한다.
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
locations_zero = []
union = [[0 for _ in range(m)] for _ in range(n)]
unions_count = {0:0}
union_number = 0
for r in range(n):
    for c in range(m):
        if not union[r][c] and graph[r][c] == 1:
            union_number += 1
            cnt = 1
            queue = deque([])
            queue.append([r, c])
            union[r][c] = union_number
            
            while queue:
                x, y = queue.popleft()
                for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    if 0<=x+dx<n and 0<=y+dy<m and graph[x+dx][y+dy] and not union[x+dx][y+dy]:
                        union[x+dx][y+dy] = union_number
                        queue.append([x+dx, y+dy])
                        cnt += 1
            unions_count[union_number] = cnt
        elif graph[r][c] == 0:
            locations_zero.append([r, c])

result = 0
for zero_x, zero_y in locations_zero:
    now_size = 1
    near_union = set([])
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if 0<=zero_x+dx<n and 0<=zero_y+dy<m:
            near_union.add(union[zero_x+dx][zero_y+dy])
    for u in near_union:
        now_size += unions_count[u]
    result = max(result, now_size)

print(result)