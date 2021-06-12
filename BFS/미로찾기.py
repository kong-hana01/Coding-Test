from collections import deque
n, m = 5, 6
map_ = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]


# 1. 큐에 현재 위치에서 동서남북에 해당하는 위치를 다 넣고 빼는 과정을 반복하며 count를 하나씩 증가시킨다.
# 2. n-1, m-1 위치에 도달할 경우 count를 리턴한다.


def bfs(n, m):
    queue = deque()
    depth = 0
    queue.append([0,0,depth])
    map_[0][0] = 0
    while queue:
        col, row, depth = queue.popleft()
        depth += 1
        for dcol, drow in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ncol, nrow = dcol+col, drow+row
            if 0 <= ncol <= n-1 and 0 <= nrow <= m-1 and map_[ncol][nrow] == 1:
                queue.append([ncol, nrow, depth])
                map_[ncol][nrow] = 0
                
        #print(col, row, depth)


        if col == n-1 and row == m-1:
            return depth

print(bfs(n,m))