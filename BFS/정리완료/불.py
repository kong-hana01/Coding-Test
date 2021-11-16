# https://www.acmicpc.net/problem/5427
# 접근 방법
# BFS를 통해 불의 움직임을 먼저 구현한 뒤, 해당 시간의 초를 각 빈공간에 저장한다.
# 이후 상근이가 현재 움직인 시간과 불이 도달한 시간을 비교해 상근이가 움직일 수 있는 공간을 큐에 삽입한다.
# 상근이에 대한 BFS를 진행한 뒤, 총 진행된 시간을 출력한다.
# 만약 상근이가 중간에 바깥으로 탈출한 경우 bfs를 종료하고 값을 출력한다.
# 만약 상근이가 모든 인덱스를 돌았지만 빌딩을 탈출할 수 없는 경우 impossible을 출력한다.
import sys
from collections import deque
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    w, h = map(int, input().split())
    board = [[x for x in input().rstrip()] for _ in range(h)]
    fire = deque([])
    sg = deque([])
    visited = [[False for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if board[i][j] == "@":
                sg.append([0, i, j])
                visited[i][j] = True
            elif board[i][j] == '*':
                fire.append([i, j])
                board[i][j] = 0
            elif board[i][j] == '#':
                visited[i][j] = True

    while fire:
        r, c = fire.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r+dr<=h-1 and 0<=c+dc<=w-1 and board[r+dr][c+dc] == '.':
                board[r+dr][c+dc] = board[r][c] + 1
                fire.append([r+dr, c+dc])
    
    time = 0
    while sg:
        t, r, c = sg.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r+dr<=h-1 and 0<=c+dc<=w-1:
                if not visited[r+dr][c+dc] and (board[r+dr][c+dc] == '.' or board[r+dr][c+dc] > t + 1):
                    sg.append([t + 1, r+dr, c+dc])
                    visited[r+dr][c+dc] = True
            else:
                time = t + 1
                break

        if time:
            break
    if time:
        print(time)
    else:
        print("IMPOSSIBLE")