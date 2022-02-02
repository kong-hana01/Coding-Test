# https://www.acmicpc.net/problem/3184
# 접근 방법
# BFS를 통해 양과 늑대의 수를 구한 뒤, 해당 값을 비교해 양과 늑대의 수를 체크하고, 최종 수를 출력한다.
def bfs(row, col):
    global countSheep, countWolf
    queue = deque([])
    queue.append([row, col])
    sheep, wolf = 0, 0
    visited[row][col] = True
    while queue:
        row, col = queue.popleft()
        if field[row][col] == 'o':
            sheep += 1
        elif field[row][col] == 'v':
            wolf += 1
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=row+dr<r and 0<=col+dc<c and not visited[row+dr][col+dc] and field[row+dr][col+dc] != '#':
                queue.append([row+dr, col+dc])
                visited[row+dr][col+dc] = True
    sheep, wolf = (sheep, 0) if sheep > wolf else (0, wolf)
    countSheep += sheep
    countWolf += wolf

from collections import deque
r, c = map(int, input().split())
field = [[x for x in input()] for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
countSheep, countWolf = 0, 0

for row in range(r):
    for col in range(c):
        if field[row][col] != '#' and not visited[row][col]:
            bfs(row, col)
print(countSheep, countWolf)