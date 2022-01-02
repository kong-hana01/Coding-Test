# https://www.acmicpc.net/problem/11123
# 접근 방법
# BFS를 통해 양의 무리를 세어본다.
def BFS(r, c):
    queue = deque([])
    queue.append([r, c])
    arr[r][c] = '.'
    while queue:
        row, col = queue.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=row+dr<h and 0<=col+dc<w and arr[row+dr][col+dc] == '#':
                queue.append([row+dr, col+dc])
                arr[row+dr][col+dc] = '.'
from collections import deque
tc = int(input())
for _ in range(tc):
    h, w = map(int, input().split())
    arr = [[x for x in input()] for _ in range(h)]
    count = 0
    for r in range(h):
        for c in range(w):
            if arr[r][c] == '#':
                BFS(r, c)
                count += 1
    print(count)