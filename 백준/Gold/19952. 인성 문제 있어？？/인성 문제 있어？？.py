# https://www.acmicpc.net/problem/19952
# 접근 방법
# BFS를 이용해 문제를 해결한다.
# BFS를 통해 먼저 접근하는 경우 남은 힘이 추후에 도달할 수 있는 상황에서의 남은 힘보다 크기에 BFS를 돌려도 괜찮다.
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, w, o, f, startX, startY, endX, endY = map(int, input().split())
    board = [[0 for _ in range(w+1)] for _ in range(h+1)]
    visited = [[f+1 for _ in range(w+1)] for _ in range(h+1)]
    for _ in range(o):
        x, y, l = map(int, input().split())
        board[x][y] = l
    queue = deque([])
    queue.append([startX, startY])
    visited[startX][startY] = f
    while queue:
        x, y = queue.popleft()
        if visited[x][y] == 0:
            continue
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 1<=x+dx<=h and 1<=y+dy<=w and visited[x+dx][y+dy] == f+1 and board[x+dx][y+dy] - board[x][y] <= visited[x][y]:
                visited[x+dx][y+dy] = visited[x][y] - 1
                queue.append([x+dx, y+dy])
    
    if visited[endX][endY] == f+1:
        print("인성 문제있어??")
    else:
        print("잘했어!!")