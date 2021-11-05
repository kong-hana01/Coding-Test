# https://www.acmicpc.net/problem/3197
# 접근 방법
# 처음 백조가 있는 위치를 기준으로 dfs를 동작시켜 얼음이 없는 위치에 1과 2의 값을 입력한다.
# 물에 닿아있는 빙판을 기준으로 bfs를 동작시키고, 주변 위치에 있는 1또는 2의 값을 그대로 이어받고, 만약 둘 다 있다면 bfs를 멈추고 count를 출력한다.
# bfs를 동작시키고, 값을 저장한 뒤, 상하좌우의 위치에 빙판이 있다면 해당 값을 큐에 저장한다. 이때 방문처리를 확인한 뒤, 방문처리가 되어있다면 큐에 삽입하지 않는다.
def dfs(row, col, num):
    board[row][col] = num
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0<=row+dr<=r-1 and 0<=col+dc<=c-1:
            if board[row+dr][col+dc] == '.':
                dfs(row+dr, col+dc, num)
            elif board[row+dr][col+dc] == (num+1) % 2:
                return True

import sys
from collections import deque
input = sys.stdin.readline
r, c = map(int, input().split())
board = [[x for x in input().rstrip()] for _ in range(r)]
check = False
count = 0
num = 0
visited = [[0 for _ in range(c)] for _ in range(r)]
queue = deque([])
swan = []
for row in range(r):
    for col in range(c):
        if board[row][col] == 'L':
            queue1 = deque([])
            queue1.append([row, col])
            board[row][col] = num
            swan.append(num)
            while queue1 and not check:
                x, y = queue1.popleft()
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if 0<=x+dx<=r-1 and 0<=y+dy<=c-1:
                        if board[x+dx][y+dy] == '.':
                            queue1.append([x+dx, y+dy])
                            board[x+dx][y+dy] = num
                        elif len(swan) >= 2 and board[x+dx][y+dy] == swan[0]:
                            check = True
                            break
            num += 1
        elif board[row][col] == "X":
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0<=row+dr<=r-1 and 0<=col+dc<=c-1 and board[row+dr][col+dc] != 'X':
                    queue.append([row, col])
                    visited[row][col] = 1
                    break

        elif board[row][col] == '.':
            board[row][col] = num
            queue1 = deque([])
            queue1.append([row, col])
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0<=row+dr<=r-1 and 0<=col+dc<=c-1 and board[row+dr][col+dc] != 'X':
                    while queue1 and not check:
                        x, y = queue1.popleft()
                        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                            if 0<=x+dx<=r-1 and 0<=y+dy<=c-1:
                                if board[x+dx][y+dy] == '.':
                                    queue1.append([x+dx, y+dy])
                                    board[x+dx][y+dy] = num
                                elif board[x+dx][y+dy] == 'L':
                                    queue1.append([x+dx, y+dy])
                                    swan.append(num)
                                    board[x+dx][y+dy] = num
            num += 1

parent = [i for i in range(num)]

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def find_union(x1, x2, check=False):
    x1 = get_parent(x1)
    x2 = get_parent(x2)
    if not check:
        if x1 < x2:
            parent[x2] = x1
            return False
        elif x1 > x2:
            parent[x1] = x2
            return False
        else:
            return True
    else:
        if x1 == x2:
            return True
if not check:
    count = 1
while queue and not check:
    row, col = queue.popleft()
    p = []
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0<=row+dr<=r-1 and 0<=col+dc<=c-1:
            if board[row+dr][col+dc] == 'X' and not visited[row+dr][col+dc]:
                queue.append([row+dr, col+dc])
                visited[row+dr][col+dc] = visited[row][col] + 1
                count = max(count, visited[row+dr][col+dc])
            elif (not p or (p and p[0] != board[row+dr][col+dc])) and type(board[row+dr][col+dc]) == type(1):
                p.append(board[row+dr][col+dc])
                if len(p) == 2:
                    find_union(p[0], p[1])
                    p.pop()

    if find_union(swan[0], swan[1], True):
        check = True

    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0<=row+dr<=r-1 and 0<=col+dc<=c-1 and board[row+dr][col+dc] == 'X':
            board[row+dr][col+dc] = p[0]

print(count)
