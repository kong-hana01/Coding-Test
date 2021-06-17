import sys, copy
from collections import deque
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
painting = [sys.stdin.readline().rstrip() for _ in range(n)]
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(row, col, target):
    visited[col][row] = True
    for drow, dcol in direction:
        
        new_row = row+drow
        new_col = col+dcol
        if 0<=new_row<=n-1 and 0<=new_col<=n-1 and not visited[new_col][new_row] and painting_[new_col][new_row] == target:
            dfs(new_row, new_col, target)



for red_green_blindness in [False, True]: 
    
    painting_ = copy.deepcopy(painting)
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0
    if red_green_blindness:
        for i in range(n):
            painting_[i] = painting[i].replace('G', 'R')   

    
    for target in ['R', 'G', 'B']:
        for col in range(n):
            for row in range(n):
                if not visited[col][row] and painting_[col][row] == target:
                    dfs(row, col, target)
                    count += 1
    print(count)