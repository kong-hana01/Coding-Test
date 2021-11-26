# https://www.acmicpc.net/problem/17070
# 접근방법 1
# 파이프의 모양에 따라 dfs 처럼 탐색하며 탐색한 위치에 +1을 해준다.
# 해당 위치의 경우의 수와, 벽의 위치를 구분하기 위해 새 집의 크기를 숫자로 받지 않고, string으로 받는다.
# 시간복잡도 위배로 인해 탐색시간 초과
# import sys
# n = int(sys.stdin.readline())
# # graph = [[0]*n for _ in range(n)]
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# steps = [[[0, 1], [1, 1], [0, 0]], [[0, 1], [1, 1], [1, 0]], [[0, 0], [1, 1], [1, 0]]] # 가로 대각선 세로 방향(인덱스 별로 가로, 대각선, 세로를 구분)
# d = 0 # 처음 파이프 위치 초기화

# def dfs(x, y, d):
#     # 최대 16 x 16의 그래프를 탐색한다는 점과 각 놓여진 위치에 따라 경우의 수가 달라진다는 점때문에 방문처리 x
#     if graph[x][y] == '0':
#         graph[x][y] = 1
#     else:
#         graph[x][y] += 1

#     for i in range(len(steps[d])):
#         dx, dy = steps[d][i]
#         if [dx, dy] == [0, 0]:
#             continue
#         elif x+dx < n and y+dy < n and graph[x+dx][y+dy] != '1':
#             dfs(x+dx, y+dy, i)

# dfs(0, 1, d)
# print(graph)


# 접근방법 2
# 각 위치에 어느 방향의 파이프로부터 연결될 수 있는 지에 대한 리스트 정보를 저장한다.
import sys
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 1:
            graph[i][j] = [1, 0, 0]
        elif graph[i][j] != 1:
            graph[i][j] = [0, 0, 0]

for i in range(n):
    for j in range(2, n):
        if graph[i][j] != 1: # 탐색하고자 하는 위치가 벽이 아니라면
            # 1. 왼쪽 위치에 있는 파이프 탐색 (가로로 놓여져 있는 경우)
            if graph[i][j-1] != 1:
                graph[i][j][0] += graph[i][j-1][0] + graph[i][j-1][1]
            # 2. 왼쪽 상단의 대각선 위치에 있는 파이프 탐색 (대각선으로 놓여져 있는 경우)
            if i > 0:
                if graph[i-1][j-1] != 1 and graph[i-1][j] != 1 and graph[i][j-1] != 1:
                    graph[i][j][1] = sum(graph[i-1][j-1])
            # 3. 위에 위치한 파이프 탐색 (세로로 놓여져 있는 경우)
                if graph[i-1][j] != 1:
                    graph[i][j][2] += graph[i-1][j][1] + graph[i-1][j][2]
if graph[n-1][n-1] != 1:
    print(sum(graph[n-1][n-1]))
else:
    print(0)            