# https://www.acmicpc.net/problem/16234
# 접근방법
# 날마다 국경을 BFS를 통해 탐색한 뒤, 연합이 있으면 그 연합의 인구수를 나누어 계산해준다.
# 연합이 없으면 며칠이 소요됐는지 날짜를 출력한다.
# 최대 연산횟수: 칸의 개수 x 인구이동이 가능한 최대 날짜 = 2500 x 1000 = 약 250만회

from collections import deque
import sys

n, l, r = map(int, sys.stdin.readline().split())
map_ = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def bfs(i, j, zone):
    queue = deque([])
    queue.append([i, j])
    visited[i][j] = zone
    union = [[i, j]]
    population = map_[i][j]
    
    # bfs 탐색 진행
    while queue:
        x, y = queue.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=x+dx<=n-1 and 0<=y+dy<=n-1 and visited[x+dx][y+dy] == 0 and l <= abs(map_[x+dx][y+dy] - map_[x][y]) <= r:
                queue.append([x+dx, y+dy])
                visited[x+dx][y+dy] = zone
                union.append([x+dx, y+dy]) # 연합 지역 리스트
                population += map_[x+dx][y+dy] # 인구 수
    
    # 형성된 연합을 기준으로 인구수 분배
    for x, y in union:
        map_[x][y] = population // len(union)
        
# 최대 2000일 이내로 결정
for k in range(0, 2000):
    zone = 1
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i, j, zone)
                zone += 1
    if zone == n ** 2 + 1:
        break
print(k)