# https://www.acmicpc.net/problem/1486
# 접근 방법
# 다익스트라로 문제를 해결한다. 단, 되돌아와야한다는 요구사항이 있기에 갈 때와 올 떄를 고려해 문제를 해결한다.
def dijkstra(r, c, distance):
    h = []
    heapq.heappush(h, [0, r, c])
    distance[r][c] = 0
    while h:
        dist, r, c = heapq.heappop(h)
        if distance[r][c] < dist:
            continue
        now = alpha_to_num[board[r][c]]
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r+dr<n and 0<=c+dc<m:
                next = alpha_to_num[board[r+dr][c+dc]]
                if abs(now - next) > t:
                    continue
                if now >= next:
                    next_dist = dist + 1
                else:
                    next_dist = dist + (next - now) ** 2
                if next_dist < distance[r+dr][c+dc] and next_dist <= d:
                    distance[r+dr][c+dc] = next_dist
                    heapq.heappush(h, [next_dist, r+dr, c+dc])

import sys, heapq
input = sys.stdin.readline
n, m, t, d = map(int, input().split())
board = [[x for x in input()] for _ in range(n)]
alpha_to_num = {}
alphabet = [chr(x) for x in range(ord('A'), ord("Z")+1)]
for i in range(len(alphabet)):
    alpha = alphabet[i]
    alpha_to_num[alpha] = i
    alpha_to_num[alpha.lower()] = i + 26
INF = int(1e7)
go_distance = [[INF for _ in range(m)] for _ in range(n)]
dijkstra(0, 0, go_distance)
max_height = alpha_to_num[board[0][0]]
for r in range(n):
    for c in range(m):
        if r == c == 0:
            continue
        distance = [[INF for _ in range(m)] for _ in range(n)]
        dijkstra(r, c, distance)
        if distance[0][0] + go_distance[r][c] <= d:
            max_height = max(max_height, alpha_to_num[board[r][c]])
print(max_height)