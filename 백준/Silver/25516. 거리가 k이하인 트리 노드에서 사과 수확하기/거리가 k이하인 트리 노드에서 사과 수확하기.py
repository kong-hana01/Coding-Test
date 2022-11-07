# https://www.acmicpc.net/problem/25516
# 접근 방법
# BFS를 통해 문제를 해결한다.
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c = map(int, input().split())
    tree[p].append(c)
apples = list(map(int, input().split()))
visited = [-1 for _ in range(n+1)]
queue = deque([])
queue.append(0)
result = 0
visited[0] = 0
while queue:
    parent = queue.popleft()
    if visited[parent] > k:
        continue
    result += apples[parent]
    for child in tree[parent]:
        visited[child] = visited[parent] + 1
        queue.append(child)
        
print(result)