# https://www.acmicpc.net/problem/14497
# 접근 방법
# 

def dijkstra(x1, y1):
    distance[x1-1][y1-1] = 0
    q = []
    heapq.heappush(q, [0, x1-1, y1-1])
    while q:
        count, x, y = heapq.heappop(q)
        if distance[x][y] < count:
            continue
            
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=x+dx<=n-1 and 0<=y+dy<=m-1:
                if board[x+dx][y+dy] == '0' and distance[x+dx][y+dy] > count:
                    heapq.heappush(q, [count, x+dx, y+dy])
                    distance[x+dx][y+dy] = count
                elif board[x+dx][y+dy] == '1' and distance[x+dx][y+dy] > count + 1:
                    heapq.heappush(q, [count+1, x+dx, y+dy])
                    distance[x+dx][y+dy] = count + 1
                elif board[x+dx][y+dy] == '#':
                    return count
                    
import heapq
n,m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
board = [[x for x in input()] for _ in range(n)]
INF = int(1e9)
distance = [[INF for _ in range(m)] for _ in range(n)]
print(dijkstra(x1, y1))