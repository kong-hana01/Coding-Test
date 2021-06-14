# 골드
# 가로와 세로의 크기가 최대 8이다.
# 빈칸이 최대인 경우는 바이러스가 1개이고, 나머지는 모두 빈칸인 경우 즉, 63개이다.
# 모든 빈칸에 벽을 3번씩 세우는 경우의 수는 63*62*61=238,266이다.
# 모든 경우에 수에 대해 BFS로 탐색할 경우 최대 61번 탐색하게 된다. 
# 따라서 BFS로 모든 경우의 수를 탐색하는 것은 63*62*61*61=14,534,226번이다.

from collections import deque
import sys, copy, time
s = time.time()
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# n, m = 7, 7
# graph = [[2, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]
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
    return result, graph_

result = 0
for i in range(len(blank)):
    for j in range(i, len(blank)):
            for k in range(j, len(blank)):
                temp, graph_ = bfs(i, j, k, count, n, m)
                result = max(result, temp)

print(time.time()-s)
print(result)     
