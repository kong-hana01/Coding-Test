# https://www.acmicpc.net/problem/4991
# 접근 방법
# 더러운 칸의 개수만큼 bfs를 돌려서 개수를 확인한다.
def bfs(r, c, i):
    visited[i][r][c] = 0
    queue = deque([])
    queue.append([r, c])
    while queue:
        r, c = queue.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r+dr<h and 0<=c+dc<w and visited[i][r+dr][c+dc] == -1 and graph[r+dr][c+dc] != "x":
                visited[i][r+dr][c+dc] = visited[i][r][c] + 1
                queue.append([r+dr, c+dc])

from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    graph = [[x for x in input()] for _ in range(h)]
    cntOfDirty = 0
    dirty = []
    for r in range(h):
        for c in range(w):
            if graph[r][c] == "*":
                cntOfDirty += 1
                dirty.append([r, c])
            elif graph[r][c] == "o":
                start = [r, c]
    visited = [[[-1 for _ in range(w)] for _ in range(h)] for _ in range(cntOfDirty+1)]
    INF = int(1e9)
    result = INF
    bfs(start[0], start[1], 0)
    for i in range(cntOfDirty):
        start = dirty[i]
        bfs(start[0], start[1], i+1)
        

    for com in list(permutations([x for x in range(1, cntOfDirty+1)], cntOfDirty)):
        r, c = dirty[com[0]-1]
        now_cnt = visited[0][r][c]
        is_fail = False
        for i in range(1, cntOfDirty):
            r, c = dirty[com[i]-1]
            now_cnt += visited[com[i-1]][r][c]
            if visited[com[i-1]][r][c] == -1:
                is_fail = True
                break
        if not is_fail and now_cnt < result:
            result = now_cnt
    if result != INF:
        print(result)
    else:
        print(-1)