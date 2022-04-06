# https://www.acmicpc.net/problem/15591
# 접근 방법
# 힙을 사용한 너비우선 탐색을 통해 다른 동영상으로 이동하는 USADO 값의 최소값을 갱신한다.
from collections import deque
n, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, q, r = map(int, input().split())
    graph[p].append([q, r])
    graph[q].append([p, r])

distance = [[0 for _ in range(n+1)] for _ in range(n+1)]
queue = deque([])
queue.append([1, 0])
while queue:
    video, usado = queue.popleft()
# 보류