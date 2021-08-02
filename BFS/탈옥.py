# https://www.acmicpc.net/problem/9376
# 추후 재도전
# 접근방법
# 각각의 죄수에 대해 문을 부순 횟수를 기록할 평면도를 따로 만든다.
# 이후 한 죄수가 문을 부수면 그 죄수의 위치에는 이전 인덱스 +1을 해주고, 다른 평면도에는 그 위치에 있는 문을 없앤다.

from collections import deque
h, w = map(int, input().split())
array = [[x for x in input()] for _ in range(h)]
queue = deque([])
visited = [[[False for _ in range(w)] for _ in range(h)] for _ in range(2)]

number = 0
for i in range(h):
    for j in range(w):
        if array[i][j] == '$':
            array[i][j] = '.'
            queue.append([number, i, j])
            visited[number][i][j] = 1
            number += 1
            
array_2 = [x[:] for x in array]


while queue:
    number, r, c = queue.popleft()

    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0<=r+dr<=h-1 and 0<=c+dc<=w-1 and not visited[number][r+dr][c+dc]:
            if array[r+dr][c+dc] == '.':
                queue.append([number, r+dr, c+dc])
                visited[number][r+dr][c+dc] = visited[number][r][c]
            elif array[r+dr][c+dc] == '#':
                queue.append([number, r+dr, c+dc])
                visited[number][r+dr][c+dc] = visited[number][r][c] + 1
                array[r+dr][c+dc] = '.'
            print(r+dr, c+dc)

print(visited)
