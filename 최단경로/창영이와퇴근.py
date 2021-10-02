# acmicpc.net/problem/22116
# 접근방법
# 다익스트라 최단경로 알고리즘을 활용해 문제를 해결한다.
def dijkstra(row, col):
    distance[row][col] = 0
    q = []
    heapq.heappush(q, [0, row, col])
    while q:
        dist, r, c = heapq.heappop(q)
        if distance[r][c] < dist:
            continue
        if r == n-1 and c == n-1:
            return
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r+dr<=n-1 and 0<=c+dc<=n-1:
                if distance[r+dr][c+dc] > max(dist, abs(board[r][c] - board[r+dr][c+dc])):
                    distance[r+dr][c+dc] = max(dist, abs(board[r][c] - board[r+dr][c+dc]))
                    heapq.heappush(q, [distance[r+dr][c+dc], r+dr, c+dc])


import heapq, sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
INF = int(1e9)
distance = [[INF for _ in range(n)] for _ in range(n)]
dijkstra(0, 0)
print(distance[-1][-1])