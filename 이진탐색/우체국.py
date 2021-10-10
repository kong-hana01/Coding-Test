# https://www.acmicpc.net/problem/2141
# 접근 방법
# 이진탐색을 통해 각 사람까지의 거리가 최소가 되는 곳의 위치를 출력한다.
import sys, math
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
start = 1e-9
end = 1e9
min_dist = math.inf
while start <= end:
    mid = (start+end) // 2
    dist = 0
    for x in array:
        dist += abs(mid - x[0]) * x[1]

    if min_dist > dist:
        end