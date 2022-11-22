from collections import deque
import sys, copy
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
blank = []
queue = deque([])
count = 0
wall_count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append([i, j])
        elif graph[i][j] == 2:
            queue.append([i, j])
            count += 1
        else:
            wall_count += 1

def bfs(i, j, k, count, n, m):
    graph_ = copy.deepcopy(graph)
    queue_ = copy.deepcopy(queue)
    for x in [i, j, k]:
        x_, y_ = blank[x]
        graph_[x_][y_] = 1
    
    while queue_:
        x, y = queue_.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=x+dx<=n-1 and 0<=y+dy<=m-1 and graph_[x+dx][y+dy] == 0:
                queue_.append([x+dx, y+dy])
                graph_[x+dx][y+dy] = 2
                count += 1

    result = (n * m) - (count+wall_count+3)
    return result

result = 0
for i in range(len(blank)):
    for j in range(i, len(blank)):
            for k in range(j, len(blank)):
                cnt = bfs(i, j, k, count, n, m)
                result = max(result, cnt)

print(result)     