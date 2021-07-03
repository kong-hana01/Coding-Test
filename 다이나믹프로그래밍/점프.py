# https://www.acmicpc.net/problem/1890
# 접근방법
# 가장 왼쪽 위 쪽에 위치한 수부터 시작해서 이동 가능한 범위에 있는 dp 테이블에 경우의 수를 입력한다.
from collections import deque
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
d = [[0 for _ in range(n)] for _ in range(n)]
d[0][0] = 1
queue = deque([])
queue.append([0, 0])
# while queue:
#     row, col = queue.popleft()

#     x = array[col][row]
#     if row+x <= n-1:
#         d[col][row+x] += d[col][row]
#         if row+x != n-1 or col != n-1:
#             queue.append([row+x, col])

#     if col+x <= n-1:
#         d[col+x][row] += d[col][row]
#         if row != n-1 or col+x != n-1:
#             queue.append([row, col+x])

# print(d[n-1][n-1])

for i in range(n):
    for j in range(n):
        if d[i][j] > 0 and array[i][j] != 0:
            x = array[i][j] # 탐색하고자하는 위치의 이동가능 칸 수 입력
            if i+x <= n-1:
                d[i+x][j] += d[i][j]
            if j+x <= n-1:
                d[i][j+x] += d[i][j]

print(d[n-1][n-1])

