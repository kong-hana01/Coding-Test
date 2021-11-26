# https://www.acmicpc.net/problem/15686
# 접근방법
# 주어진 도시의 정보 중 치킨집이 위치할 수 있는 곳에 대해 모든 경우의 수를 고려한 뒤, 치킨 거리가 가장 적은 거리를 출력한다.
import sys
from collections import deque
from itertools import combinations

# 시간복잡도 체크
# 최대 연산 횟수: N x N x 13C6 = 50 x 50 x 1716 = 약 430만회
v = 0
for i in range(1, 14):
    x = len(list(combinations([x for x in range(1, 14)], i)))
    v = max(v, x)
# print(v * 2500) >>> 4290000

# 문제 풀이
n, m = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
house = []
chickens = []
CountOfHouse = 0 

for x in range(n):
    for y in range(n):
        if city[x][y] == 1:
            CountOfHouse += 1
        if city[x][y] == 2:
            chickens.append([x, y])
            city[x][y] = 0

result = 2500 * 100  # 결과값 최대값으로 초기화
for chicken in list(combinations(chickens, m)): # 치킨집의 경우의 수
    map_ = [x[:] for x in city]
    queue = deque([])
    distance = 0 # 치킨거리 초기화
    count = 0
    for x in chicken: # 치킨집의 위치 큐에 저장
        map_[x[0]][x[1]] = 2
        queue.append([x[0], x[1]])
    
    # BFS 탐색
    while queue:
        x, y = queue.popleft()

        for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
            if 0<=x+dx<=n-1 and 0<=y+dy<=n-1:
                if map_[x+dx][y+dy] == 1:
                    queue.append([x+dx, y+dy])
                    map_[x+dx][y+dy] = map_[x][y] + 1
                    distance += map_[x+dx][y+dy] - 2 # 집에 도착할 경우 치킨 거리를 누적
                    count += 1

                elif map_[x+dx][y+dy] == 0:
                    queue.append([x+dx, y+dy])
                    map_[x+dx][y+dy] = map_[x][y] + 1
        
        if CountOfHouse == count:
            break    
    result = min(result, distance) # 매 경우의 수마다 최소 치킨거리 저장

print(result) # 최소 치킨 거리 출력