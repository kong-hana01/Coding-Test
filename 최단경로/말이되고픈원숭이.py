# https://www.acmicpc.net/problem/1600
# 접근 방법
# 다익스트라 알고리즘을 활용해 이동한 동작의 최소값을 구한다.
def dijkstra():
    distance[0][0][0] = 0
    H = []
    heapq.heappush(H, [0, 0, 0, 0]) # count, 말 이동 횟수, row, col
    while H:
        dist, count, row, col = heapq.heappop(H)
        if distance[count][row][col] < dist:
            continue
        for dr, dc, c in [[0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0], [2, 1, 1], [2, -1, 1], [1, 2, 1], [-1, 2, 1], [1, -2, 1], [-1, -2, 1], [-2, 1, 1], [-2, -1, 1]]:
            if 0<=row+dr<h and 0<=col+dc<w and count+c <= k and not board[row+dr][col+dc] and distance[count+c][row+dr][col+dc] > dist + 1:
                distance[count+c][row+dr][col+dc] = dist + 1
                heapq.heappush(H, [dist+1, count+c, row+dr, col+dc])
        
import heapq
k = int(input())
w, h = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(h)]
INF = int(1e5)
distance = [[[INF for _ in range(w)] for _ in range(h)] for _ in range(k+1)]
dijkstra()
minCount = INF
for i in range(k+1):
    minCount = min(minCount, distance[i][-1][-1])
print(minCount if minCount != INF else -1)