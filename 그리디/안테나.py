# https://www.acmicpc.net/problem/18310
# 접근 방법
# 1. 한 방향에서부터 자신보다 진행하는 방향의 반대편에 위치한 집의 개수를 세어 그 전 집에서부터의 현재 집까지의 거리를 곱해 현재 방향으로 이동할 때까지의 거리를 계산한다.
# 2. 반대편도 마찬가지로 계산한다.
# 3. 거리를 합하여 가장 거리가 짧은 집을 선택한다.
def calc_dist(house, reverse):
    if reverse:
        house = house[::-1]
    now = house[0]
    last = house[0]
    for i in range(1, n):
        now = house[i]
        dist[reverse][now] = dist[reverse][last] + abs(now - last) * i
        last = house[i]
    

import sys
input = sys.stdin.readline
n = int(input())
house = list(map(int, input().split()))
house.sort()
dist = [[0 for _ in range(100001)] for _ in range(2)]
for i in range(2):
    calc_dist(house[:], i)

total_dist = [[dist[0][i] + dist[1][i], i] for i in range(100001) if dist[0][i] + dist[1][i]]
min_dist = int(1e11)
result = house[0]

for distance, idx in total_dist:
    if distance < min_dist:
        min_dist = distance
        result = idx
print(result)