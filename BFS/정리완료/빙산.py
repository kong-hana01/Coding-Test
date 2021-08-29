# https://www.acmicpc.net/problem/2573
# 접근 방법
# 이차원 배열을 입력받으면서 현재 빙산이 있는 위치를 저장하고 방문처리를 위한 배열에 1의 값을 저장하고, 해당 위치에 대해 매번 상하좌우를 탐색하여 물이 있다면 수를 줄여준다. 만약 빙산이 없어진 경우 방문처리를 위한 배열에 0을 저장한다.
# 빙산을 녹일 때 빙산이 남아있다면 그 위치를 저장하고 방문처리를 위한 배열의 해당 위치에 1씩 더 더해준다. 빙산이 있는 위치 중 하나에서 BFS를 탐색한다.
# 만약 BFS를 통해 연결되어있는 빙산의 개수와 비교해 더 작다면 지난 시간을 출력한다.
# 만약 빙산이 없다면 0을 출력한다.
def melting_iceberg(iceberg):
    temp = []
    count_ = [0 for _ in range(len(iceberg))]
    for i in range(len(iceberg)):
        row, col = iceberg[i]
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if array[row+dr][col+dc] == 0:
                count_[i] += 1
    for i in range(len(iceberg)):
        row, col = iceberg[i]
        array[row][col] = max(0, array[row][col] - count_[i])
        if array[row][col]:
            temp.append([row, col])

    return temp

def bfs(time):
    if not iceberg:
        return 0
    queue = deque([])
    queue.append(iceberg[0])
    visit[iceberg[0][0]][iceberg[0][1]] += 1
    count = 1
    while queue:
        row, col = queue.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if visit[row+dr][col+dc] == time and array[row+dr][col+dc]:
                queue.append([row+dr, col+dc])
                
                visit[row+dr][col+dc] += 1
                count += 1
    return count

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

iceberg = []
visit = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if array[i][j] > 0:
            iceberg.append([i, j])
            visit[i][j] = 1

time = 0
while True:
    iceberg = melting_iceberg(iceberg)
    time += 1
    count = bfs(time)
    if not iceberg:
        print(0)
        break
    elif len(iceberg) != count:
        print(time)
        break
