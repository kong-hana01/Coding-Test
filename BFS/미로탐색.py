from collections import deque
import sys

# n, m = map(int, sys.stdin.readline().split())
#map_ = [list(map(int, list(str(sys.stdin.readline()))[:m])) for _ in range(n)]

n, m = 2, 6
map_ = [list(map(int, input())) for _ in range(n)]
# map_ = [[1,0,1,1,1,1], [1,0,1,0,1,0], [1,0,1,0,1,1], [1,1,1,0,1,1]]
step_ = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 동서남북
visited = []
def bfs():
    queue = deque()
    queue.append([0, 0, 1])
    check = False
    while queue:
        x, y, count = queue.popleft()
        map_[x][y] = count

        for dx, dy in step_:
            if 0 <= x+dx <= n-1 and 0 <= y+dy <= m-1 and map_[x+dx][y+dy] == 1 and [x+dx, y+dy] not in visited:
                visited.append([x+dx, y+dy])
                queue.append([x+dx, y+dy, count+1])
                if x+dx == n-1 and y+dy == m-1:
                    check = True
                    break
        if check:
            print(count+1)
            break

#bfs()
# print(map_[n-1][m-1])
print(map_)



n, m = map(int, sys.stdin.readline().split())
map_ = [list(map(int, list(str(sys.stdin.readline()))[:m])) for _ in range(n)]
step_ = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 동서남북

def bfs():
    queue = deque()
    queue.append([0, 0])
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in step_:
            if 0 <= x+dx <= n-1 and 0 <= y+dy <= m-1 and map_[x+dx][y+dy] == 1:
                queue.append([x+dx, y+dy])
                map_[x+dx][y+dy] = map_[x][y] + 1

bfs()
print(map_[n-1][m-1])