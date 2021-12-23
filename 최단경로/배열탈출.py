# https://www.acmicpc.net/problem/11909
# 접근 방법
# 다익스트라 최단경로 알고리즘을 통해 비용을 기준으로 하는 최소힙으로 이동해가며, 값을 갱신해나간다.
def dijkstra(row, col):
    h = []
    heapq.heappush(h, [0, row, col])
    INF = int(1e9)
    while h:
        cost, r, c = heapq.heappop(h)
        if board[r][c] == INF:
            continue
        now = board[r][c]
        board[r][c] = INF
        if r == n-1 and c == n-1:
            return cost
        for dr, dc in [[1, 0], [0, 1]]:
            if 0<=r+dr<n and 0<=c+dc<n and board[r+dr][c+dc] != INF:
                next_cost = cost if now > board[r+dr][c+dc] else board[r+dr][c+dc] - now + 1 + cost
                heapq.heappush(h, [next_cost, r+dr, c+dc])


import heapq, sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
print(dijkstra(0, 0), )