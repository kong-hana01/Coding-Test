# https://www.acmicpc.net/problem/6087
# 접근 방법
# 다익스트라 최단경로 알고리즘을 활용해 현재 위치에서 상하좌우로 이동한다.
# 이때 *나 범위를 벗어나게 될 경우 거울 설치 개수를 하나 늘린다.
# 이후 다른 c에 도착한다면 해당 위치에서의 거울 설치 개수를 출력한다.
def dijkstra():
    r, c = target[0]
    graph[r][c] = 0
    q = []
    for i in range(4):
        heapq.heappush(q, [0, r, c, i])
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        count, row, col, dir = heapq.heappop(q)
        if graph[row][col] not in ['.', '*'] and graph[row][col] < count:
            continue
        for i in range(4):
            dr, dc = direction[i]
            num = count + 1
            if i == dir:
                num = count
            if 0<=row+dr<h and 0<=col+dc<w:
                if graph[row+dr][col+dc] in ['.', 'C'] or (type(graph[row+dr][col+dc]) == type(1) and graph[row+dr][col+dc] >= num):
                    graph[row+dr][col+dc] = num
                    heapq.heappush(q, [num, row+dr, col+dc, i])  
                
import heapq
w, h = map(int, input().split())
graph = [[x for x in input()] for _ in range(h)]
target = []
for r in range(h):
    for c in range(w):
        if graph[r][c] == 'C':
            target.append([r, c])
dijkstra()
r, c = target[1]
print(graph[r][c])