# https://www.acmicpc.net/problem/11559
# 접근 방법
# 뿌요가 터지는 것은 BFS를 통해 동작하게끔하고, 뿌요가 아래로 떨어지는 것을 구현한다.
from collections import deque
def bfs(r, c):
    queue = deque([])
    queue.append([r, c])
    nowGroup = []
    while queue:
        row, col = queue.popleft()
        visited[row][col] = True
        nowGroup.append([row, col])
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=row+dr<12 and 0<=col+dc<6 and not visited[row+dr][col+dc] and field[row+dr][col+dc] == field[r][c]:
                queue.append([row+dr, col+dc])
                visited[row+dr][col+dc] = True
    return nowGroup if len(nowGroup) >= 4 else []

def drop():
    for r in range(10, -1, -1):
        for c in range(6):
            row = r
            while row < 11 and  field[row][c] != '.' and field[row+1][c] == '.':
                field[row][c], field[row+1][c] = field[row+1][c], field[row][c]
                row += 1
    

field = [[x for x in input()] for _ in range(12)]
count = 0
while True:
    is_finish = True
    visited = [[False for _ in range(6)] for _ in range(12)]
    popGroup = []
    for r in range(12):
        for c in range(6):
            if field[r][c] != '.' and not visited[r][c]:
                nowGroup = bfs(r, c)
                if nowGroup:
                    popGroup.extend(nowGroup)
                    is_finish = False
    
    for r, c in popGroup:
        field[r][c] = '.'
    drop()
    if is_finish:
        break
    count += 1
print(count)