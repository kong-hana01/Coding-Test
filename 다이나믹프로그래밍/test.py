import sys
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 접근방법 2
# 각 위치에 어느 방향의 파이프로부터 연결될 수 있는 지에 대한 리스트 정보를 저장한다.
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