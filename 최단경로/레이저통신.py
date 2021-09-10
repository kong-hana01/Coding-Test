# https://www.acmicpc.net/problem/6087
# 접근 방법
# 현재 방향에서 다른 방향으로 이동한 것을 최소 힙에 삽입하여 최단경로를 구한다.


def dijkstra(row, col):
    count[row][col] = 0
    q = []
    for i in range(4):
        heapq.heappush(q, [0, i, row, col])
    while q:
        count_, d, r, c = heapq.heappop(q)
        if count[r][c] < count_:
            continue
        dr, dc = direction[d]

        if 0<=r+dr<=h-1 and 0<=c+dc<=w-1 and count[r+dr][c+dc] > count_:
            if board[r+dr][c+dc] == '.':
                heapq.heappush(q, [count_, d, r+dr, c+dc])
                count[r+dr][c+dc] = count_
            elif board[r+dr][c+dc] == 'C':
                count[r+dr][c+dc] = count_

        for i in range(4):
            dr_, dc_ = direction[i]
            if i != d and 0<=r+dr_<=h-1 and 0<=c+dc_<=w-1 and board[r+dr_][c+dc_] != '*': #and count[r+dr_][c+dc_] >= count_+1:
                heapq.heappush(q, [count_+1, i, r+dr_, c+dc_])
                count[r+dr_][c+dc_] = min(count_+1, count[r+dr_][c+dc_])


import heapq
w, h = map(int, input().split())
board = [[x for x in input()] for _ in range(h)]
INF = int(1e9)
count = [[INF for _ in range(w)] for _ in range(h)]
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
target = []
for r in range(h):
    for c in range(w):
        if board[r][c] == 'C':
            target.append([r, c])
dijkstra(target[0][0], target[0][1])
print(count[target[1][0]][target[1][1]])