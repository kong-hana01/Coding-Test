import sys
from collections import deque
import copy

# 2가 위치한 곳에서 상하좌우로 범위를 하나씩 늘려간다.
# 2가 위치한 곳으로부터 일정 거리를 두고 1에 도달한다면 count를 하나씩 해서 m이 될 때까지 더한다.
# 만약 동일한 위치에 다른 2에서 출발한 것이 도달한다면(또 다른 치킨집), 최솟값으로 처리한다.
# 보류

n, m = map(int, sys.stdin.readline().split())
map_ = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
house = []
for x in range(n):
    for y in range(n):
        if map_[x][y] == 1:
            house.append([x,y])

#map_ = [[0, 0, 1, 0, 0], [0, 0, 2, 0, 1], [0, 1, 2, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 2]]

def bfs():
    result = copy.deepcopy(map_)
    queue = deque([])
    for x in range(n):
        for y in range(n):
            if result[x][y] == 2:
                queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
            if 0<=x+dx<=n-1 and 0<=y+dy<=n-1 and result[x+dx][y+dy] < 2:
                result[x+dx][y+dy] = result[x][y] + 1
                queue.append([x+dx, y+dy])
        
            count = 0
            for x_, y_ in house:
                if result[x_][y_] != 1:
                    count += 1

        if count == len(house):
            break

    return result

result = bfs()
count = 0
for x, y in house:
    count += result[x][y] - 2

print(count)